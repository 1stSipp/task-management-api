// Task Manager - Client-side JavaScript

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(flash => {
        setTimeout(() => {
            flash.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(() => flash.remove(), 300);
        }, 5000);
    });
});

// Animation for slide out
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Utility function to format dates
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
}

// Utility function to show notifications
function showNotification(message, type = 'info') {
    const flashContainer = document.querySelector('.flash-container') || createFlashContainer();
    const flash = document.createElement('div');
    flash.className = `flash flash-${type}`;
    flash.innerHTML = `
        ${message}
        <button onclick="this.parentElement.remove()" class="flash-close">&times;</button>
    `;
    flashContainer.appendChild(flash);

    setTimeout(() => {
        flash.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => flash.remove(), 300);
    }, 5000);
}

function createFlashContainer() {
    const container = document.createElement('div');
    container.className = 'flash-container';
    document.body.insertBefore(container, document.querySelector('.main-content'));
    return container;
}
