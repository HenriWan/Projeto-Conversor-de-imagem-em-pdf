// script.js - Lida com upload, envio para o backend e download do PDF gerado

// Captura elementos do DOM necessários
const form = document.getElementById('convert-form');
const uploadSection = document.getElementById('upload-section');
const downloadSection = document.getElementById('download-section');
const downloadLink = document.getElementById('download-link');
const progressContainer = document.getElementById('progress-container');
const progressBar = document.getElementById('progress-bar');

// Adiciona um ouvinte de evento ao formulário, para capturar o envio
form.addEventListener('submit', async (e) => {
  e.preventDefault(); // Evita o comportamento padrão do formulário

  const fileInput = document.getElementById('image-input');
  const formatSelect = document.getElementById('image-format');

  // Verifica se um arquivo foi selecionado
  if (fileInput.files.length === 0) {
    alert('Por favor, selecione uma imagem.');
    return;
  }

  // Prepara os dados para envio
  const formData = new FormData();
  formData.append('image', fileInput.files[0]); // Adiciona imagem ao corpo do formulário

  // Define o tipo de formato selecionado (png ou jpg)
  const formatValue = formatSelect.value;
  let format = '';
  if (formatValue.includes('png')) {
    format = 'png';
  } else if (formatValue.includes('jpg') || formatValue.includes('jpeg')) {
    format = 'jpg';
  }
  formData.append('format', format); // Adiciona formato ao corpo do formulário

  // Exibe a barra de progresso
  progressContainer.style.display = 'block';
  progressBar.style.width = '0%';

  // Simulação da barra de progresso (visual apenas)
  let progress = 0;
  const intervalTime = 100;      // Atualiza a cada 100ms
  const totalTime = 2000;        // Duração total simulada: 2 segundos
  const increment = 100 / (totalTime / intervalTime); // Valor de incremento

  // Intervalo que atualiza a barra de progresso
  const progressInterval = setInterval(() => {
    progress += increment;
    if (progress > 100) progress = 100;
    progressBar.style.width = `${progress}%`;
  }, intervalTime);

  try {
    console.log('Enviando imagem para o backend...');

    // Envia requisição para o backend com a imagem
    const response = await fetch('http://127.0.0.1:8000/convert', {
      method: 'POST',
      body: formData
    });

    // Para a barra de progresso
    clearInterval(progressInterval);
    progressBar.style.width = '100%';

    // Verifica se houve erro
    if (!response.ok) {
      console.error('Erro na resposta do backend:', response.statusText);
      alert('Erro ao converter a imagem.');
      progressContainer.style.display = 'none';
      return;
    }

    // Recebe o PDF em formato blob e gera URL temporária
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    // Atualiza o link de download
    downloadLink.href = url;
    downloadLink.download = 'convertido.pdf';

    // Alterna seções de exibição
    uploadSection.style.display = 'none';
    downloadSection.style.display = 'block';
    progressContainer.style.display = 'none';

  } catch (error) {
    clearInterval(progressInterval);
    progressContainer.style.display = 'none';
    console.error('Erro ao conectar com o backend:', error);
    alert('Erro ao conectar com o servidor.');
  }
});
