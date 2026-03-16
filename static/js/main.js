// Scroll Reveal Animation Initialization
document.addEventListener('DOMContentLoaded', () => {
  const reveals = document.querySelectorAll('.reveal');

  const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const elementVisible = 100; // Trigger point

    reveals.forEach((reveal) => {
      const elementTop = reveal.getBoundingClientRect().top;
      if (elementTop < windowHeight - elementVisible) {
        reveal.classList.add('active');
      }
    });
  };

  // Initial check and event listener
  revealOnScroll();
  window.addEventListener('scroll', revealOnScroll);

  // Form Interactions
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        // Change text to indicate loading state
        const originalText = submitBtn.innerText;
        submitBtn.innerHTML = 'Processing... <span class="spinner"></span>';
        submitBtn.style.opacity = '0.8';
        submitBtn.disabled = true;
        
        // The form will continue submitting as normal after this small visual update, 
        // to show the users that action is happening before the reload.
        setTimeout(() => {
            // Failsafe reset if the navigation takes too long or is prevented
            submitBtn.innerHTML = originalText;
            submitBtn.style.opacity = '1';
            submitBtn.disabled = false;
        }, 5000);
      }
    });
  });
});
