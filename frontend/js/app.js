const button = document.getElementById('healthBtn');
const result = document.getElementById('result');

const API_BASE_URL =
  window.location.hostname.includes('-3001.')
    ? `${window.location.protocol}//${window.location.hostname.replace('-3001.', '-8000.')}`
    : 'http://127.0.0.1:8000';

button.addEventListener('click', async () => {
  result.textContent = 'Checking...';

  try {
    const response = await fetch(`${API_BASE_URL}/api/health`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();

    result.textContent = `${data.service} backend: ${data.status}`;
  } catch (error) {
    console.error(error);
    result.textContent = 'Backend is not reachable yet.';
  }
});
