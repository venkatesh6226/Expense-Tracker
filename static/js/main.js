$(document).ready(function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);

        $('form:not(#loginForm):not(#signupForm):not(#salaryForm):not(#expenseForm):not(#editExpenseForm):not(#savingForm):not(#editSavingForm):not(#investmentForm):not(#editInvestmentForm)').on('submit', function(e) {
        var form = $(this);
        var submitBtn = form.find('button[type="submit"]');
        
        submitBtn.prop('disabled', true);
        
        setTimeout(function() {
            submitBtn.prop('disabled', false);
        }, 3000);
    });

    $('input[type="date"]').attr('max', new Date().toISOString().split('T')[0]);
    var searchTimeout;
    $('input[name="search"]').on('input', function() {
        clearTimeout(searchTimeout);
        var input = $(this);
        searchTimeout = setTimeout(function() {
            if (input.val().length >= 3 || input.val().length === 0) {
                input.closest('form').submit();
            }
        }, 500);
    });

    Object.keys(localStorage).forEach(function(key) {
        if (key.startsWith('form_')) {
            localStorage.removeItem(key);
        }
    });


        $('button[type="submit"]:not(#submitBtn):not(#expenseForm button):not(#editExpenseForm button):not(#savingForm button):not(#editSavingForm button):not(#investmentForm button):not(#editInvestmentForm button)').on('click', function() {
        var btn = $(this);
        var originalText = btn.html();
        
        btn.html('<span class="spinner-border spinner-border-sm me-2" role="status"></span>Processing...');
        btn.prop('disabled', true);
        
        setTimeout(function() {
            btn.html(originalText);
            btn.prop('disabled', false);
        }, 5000);
    });

    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        var target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top - 70
            }, 500);
        }
    });

    $('.card').addClass('fade-in');
    $('.progress-bar').each(function() {
        var progressBar = $(this);
        var width = progressBar.attr('style').match(/width:\s*(\d+(?:\.\d+)?)%/);
        if (width) {
            progressBar.css('width', '0%');
            setTimeout(function() {
                progressBar.css('width', width[1] + '%');
            }, 500);
        }
    });
    $('.table tbody tr').hover(
        function() {
            $(this).addClass('table-active');
        },
        function() {
            $(this).removeClass('table-active');
        }
    );
    $('.modal').on('hidden.bs.modal', function() {
        $(this).find('form')[0].reset();
        $(this).find('.is-invalid').removeClass('is-invalid');
    });
    $('input[required], select[required]').on('blur', function() {
        var field = $(this);
        if (!field.val()) {
            field.addClass('is-invalid');
        } else {
            field.removeClass('is-invalid');
        }
    });
    $('input[type="number"]').on('input', function() {
        var field = $(this);
        var value = parseFloat(field.val());
        var min = parseFloat(field.attr('min'));
        
        if (field.val() && (isNaN(value) || (min && value < min))) {
            field.addClass('is-invalid');
        } else {
            field.removeClass('is-invalid');
        }
    });
    $('input[type="email"]').on('blur', function() {
        var field = $(this);
        var email = field.val();
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (email && !emailRegex.test(email)) {
            field.addClass('is-invalid');
        } else {
            field.removeClass('is-invalid');
        }
    });
    $('input[name="confirm_password"]').on('input', function() {
        var confirmField = $(this);
        var passwordField = $('input[name="password"]');
        
        if (confirmField.val() && confirmField.val() !== passwordField.val()) {
            confirmField.addClass('is-invalid');
        } else {
            confirmField.removeClass('is-invalid');
        }
    });
    $('select[name="category"]:not(#expenseForm select, #savingForm select, #investmentForm select), select[name="type"]:not(#expenseForm select, #savingForm select, #investmentForm select)').on('change', function() {
        $(this).closest('form').submit();
    });

    $('.print-btn').on('click', function() {
        window.print();
    });

    $('.export-btn').on('click', function() {
        alert('Export functionality will be implemented in future versions.');
    });

    $('.theme-toggle').on('click', function() {
        $('body').toggleClass('dark-theme');
        localStorage.setItem('theme', $('body').hasClass('dark-theme') ? 'dark' : 'light');
    });

    var savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        $('body').addClass('dark-theme');
    }

    $(document).on('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.keyCode === 83) {
            e.preventDefault();
            $('form:visible').first().submit();
        }
        
        if (e.keyCode === 27) {
            $('.modal.show').modal('hide');
        }
    });
    function handleResponsiveTables() {
        $('.table-responsive').each(function() {
            var table = $(this);
            if (table[0].scrollWidth > table[0].clientWidth) {
                table.addClass('table-scroll-indicator');
            }
        });
    }

    $(window).on('resize', function() {
        handleResponsiveTables();
        if (window.chartInstances) {
            window.chartInstances.forEach(function(chart) {
                chart.resize();
            });
        }
    });

    window.chartInstances = [];
});
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

function formatDate(date) {
    return new Date(date).toLocaleDateString('en-IN');
}

function showToast(message, type = 'info') {
    var toastHtml = `
        <div class="toast align-items-center text-white bg-${type} border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    `;
    
    var toastContainer = $('.toast-container');
    if (!toastContainer.length) {
        toastContainer = $('<div class="toast-container position-fixed bottom-0 end-0 p-3"></div>');
        $('body').append(toastContainer);
    }
    
    toastContainer.append(toastHtml);
    
    var toast = new bootstrap.Toast(toastContainer.find('.toast').last()[0]);
    toast.show();
    
    toastContainer.find('.toast').last().on('hidden.bs.toast', function() {
        $(this).remove();
    });
}

function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

function debounce(func, wait) {
    var timeout;
    return function() {
        var context = this, args = arguments;
        var later = function() {
            timeout = null;
            func.apply(context, args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

window.ExpenseTracker = {
    formatCurrency: formatCurrency,
    formatDate: formatDate,
    showToast: showToast,
    confirmAction: confirmAction,
    debounce: debounce
};