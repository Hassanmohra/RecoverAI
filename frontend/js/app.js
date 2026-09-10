const button = document.getElementById('healthBtn');
const result = document.getElementById('result');
button.addEventListener('click', async () => {
  result.textContent = 'Checking...';
  try {
    const response = await fetch('http://127.0.0.1:8000/api/health');
    const data = await response.json();
    result.textContent = `${data.service} backend: ${data.status}`;
  } catch (error) {
    result.textContent = 'Backend is not reachable yet.';
  }
});
