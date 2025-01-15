import { Configuration, DefaultApi } from "./generated/index";

const config = new Configuration({
  basePath: '/api',
})

const api = new DefaultApi(config);

document.getElementById('greet-btn')!.addEventListener('click', async () => {
  const response = await api.greetsGet();
  document.getElementById('output')!.textContent = response.message ?? '';
});

document.getElementById('calc-btn')!.addEventListener('click', async () => {
  const response = await api.calculatePost({ calculatePostRequest: { num1: 5, num2: 10 } });
  document.getElementById('output')!.textContent = `Result: ${response.result}`;
});
