   // JavaScript для управления вкладками
   document.addEventListener("DOMContentLoaded", function() {
    // Получение всех элементов вкладок
    var tabs = document.querySelectorAll(".tabs div");
    
    // Получение всех элементов содержимого вкладок
    var tabContents = document.querySelectorAll(".tab-content");
    
    // Прикрепление обработчика событий щелчка на каждой вкладке
    tabs.forEach(function(tab, index) {
      tab.addEventListener("click", function() {
        // Скрытие всех содержимых вкладок
        tabContents.forEach(function(content) {
          content.classList.remove("active");
        });
        
        // Отображение только выбранного содержимого вкладки
        tabContents[index].classList.add("active");
        
        // Удаление класса "active" у всех вкладок
        tabs.forEach(function(tab) {
          tab.classList.remove("active");
        });
        
        // Добавление класса "active" к выбранной вкладке
        tab.classList.add("active");
      });
    });
  });