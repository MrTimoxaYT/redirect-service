document.addEventListener('DOMContentLoaded', function() {
    // Находим кнопку по ее идентификатору
    var copyButton = document.getElementById('copyButton');
    

    // Находим элемент <h5> с классом 'shorted_redirect_url'
    var redirectUrlElement = document.querySelector('h4.shorted_redirect_url');
    // var redirectUrlElement = document.geshorted_redirect_url('shorted_redirect_url')
    
    // Проверяем, что оба элемента существуют
    if (copyButton && redirectUrlElement) {
      // Назначаем обработчик события на нажатие кнопки
      copyButton.addEventListener('click', function() {
        // Копируем значение из элемента
        var redirectUrl = redirectUrlElement.textContent;
        
        // Создаем временный элемент input для копирования в буфер обмена
        var tempInput = document.createElement('input');
        tempInput.setAttribute('value', redirectUrl);
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
        

        

      });
    }
  });

const btn = document.getElementById('copyButton');

 
  btn.addEventListener('click', function handleClick() {
  btn.textContent = 'Copyed!';


  setTimeout(function() {btn.textContent = 'Copy';}, 2500);
    
});