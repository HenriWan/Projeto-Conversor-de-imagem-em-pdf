// script.js - Lida com upload, envio para o backend e download do PDF gerado

const form = document.getElementById('convert-form');
const uploadSection = document.getElementById('upload-section');
const downloadSection = document.getElementById('download-section');
const downloadLink = document.getElementById('download-link');
const progressContainer = document.getElementById('progress-container');
const progressBar = document.getElementById('progress-bar');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById('image-input');
  const formatSelect = document.getElementById('image-format');

  if (fileInput.files.length === 0) {
    alert('Por favor, selecione uma imagem.');
    return;
  }
