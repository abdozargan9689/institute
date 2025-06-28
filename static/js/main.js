// Main JavaScript file for Institute Management System

document.addEventListener('DOMContentLoaded', function() {
    // Add current year to footer
    const footerYear = document.querySelector('footer p');
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.innerHTML = footerYear.innerHTML.replace('{{ current_year }}', currentYear);
    }
    
    // Enable tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Enable popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Print functionality
    const printButtons = document.querySelectorAll('.btn-print');
    if (printButtons) {
        printButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                window.print();
            });
        });
    }
    
    // Search form validation
    const searchForms = document.querySelectorAll('form[action*="search"]');
    if (searchForms) {
        searchForms.forEach(form => {
            form.addEventListener('submit', function(e) {
                const searchInput = this.querySelector('input[type="search"], input[name="q"], input[name="search"]');
                if (searchInput && searchInput.value.trim() === '') {
                    e.preventDefault();
                    alert('الرجاء إدخال نص للبحث');
                }
            });
        });
    }
});