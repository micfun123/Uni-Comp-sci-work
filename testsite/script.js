let currentSectionIndex = 0;
const sections = document.querySelectorAll('.section');
const totalSections = sections.length;
let isTransitioning = false; // Prevent multiple scroll events during a transition

window.addEventListener('wheel', (event) => {
  if (isTransitioning) return; // Prevent transition if it's already happening
  const delta = event.deltaY;

  if (delta > 0) {
    // Scrolling down
    nextSection();
  } else if (delta < 0) {
    // Scrolling up
    prevSection();
  }
});

function nextSection() {
  if (currentSectionIndex < totalSections - 1) {
    currentSectionIndex++;
    updateSection();
  }
}

function prevSection() {
  if (currentSectionIndex > 0) {
    currentSectionIndex--;
    updateSection();
  }
}

function updateSection() {
  isTransitioning = true; // Start the transition
  sections.forEach((section, index) => {
    if (index === currentSectionIndex) {
      section.classList.add('active');
    } else {
      section.classList.remove('active');
    }
  });
  
  // Wait for transition to end before allowing new scroll event
  setTimeout(() => {
    isTransitioning = false;
  }, 1000); // This timeout matches the CSS transition duration
}

// Initially set the first section to be active
updateSection();
