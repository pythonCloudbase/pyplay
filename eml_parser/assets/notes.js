function resize (textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight+'px';
  }
  
  let textareas = document.querySelectorAll('.textarea-auto');
  textareas.forEach(el => {
    el.addEventListener('input', () => {
      resize(el);
    });
  })