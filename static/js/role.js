      // Get the login modal
      var loginModal = document.getElementById("loginModal");
      var modalTitle = document.getElementById("modal-title");
      var modalContent = document.getElementById("modal-content");

      // Function to open the login modal
      function openLoginModal(contentType) {
        loginModal.style.display = "block";
        modalTitle.textContent = contentType;

        // Clear previous content
        modalContent.innerHTML = "";

        if (contentType === "HTML") {
          modalContent.innerHTML = (
            `<a
              href="https://www.w3schools.com/html"
              target="_blank"
              style="color:#a770fa;"
            >
              HTML Learning Link!
            </a>`
          );
        } else if (contentType === "CSS") {
          modalContent.innerHTML = (
            `<a
              href="https://www.w3schools.com/css/"
              target="_blank"
              style="color:#a770fa;"
            >
              CSS Learning Link!
            </a>`
          );
        } else if (contentType === "JavaScript") {
          modalContent.innerHTML = (
            `<a
              href="https://www.w3schools.com/js/"
              target="_blank"
              style="color:#a770fa;"
            >
              JavaScript Learning Link!
            </a>`
          );
        } else if (contentType === "React") {
          modalContent.innerHTML = (
            `<a href="https://react.dev/" target="_blank" style="color:#a770fa;">
              React Learning Link!
            </a>`
          );
        } else if (contentType === "Angular") {
          modalContent.innerHTML = (
            `<a
              href="https://angular.io/"
              target="_blank"
              style="color:#a770fa;"
            >
              Angular Learning Link!
            </a>`
          );
        } else if (contentType === "Vue.js") {
          modalContent.innerHTML = (
            `<a href="https://vuejs.org/" target="_blank" style="color:#a770fa;">
              Vue.js Learning Link!
            </a>`
          );
        } else if (contentType === "Bookmarks") {
          modalContent.innerHTML = `<p style="color:#eee;">Please sign in to access your bookmarks.</p>
                 <div class="login-options">
                    <a href="#" class="login-button google">Sign in with Google</a>
                    <a href="#" class="login-button facebook">Sign in with Facebook</a>
                </div>
                <div class="auth-separator">OR</div>
                <div class="auth-form">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button type="submit">Sign In</button>
                    <p>Don't have an account? <a href="#" style="color:#a770fa;">Sign Up</a></p>
                </div>
                <div class="auth-separator">OR</div>
                <div class="auth-form">
                    <input type="text" placeholder="Username">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button type="submit">Sign Up</button>
                    <p>Already have an account? <a href="#" style="color:#a770fa;">Sign In</a></p>
                </div>`;
        } else {
          modalContent.innerHTML = `<p style="color:#eee;">Please sign in to access this content.</p>
                 <div class="login-options">
                    <a href="#" class="login-button google">Sign in with Google</a>
                    <a href="#" class="login-button facebook">Sign in with Facebook</a>
                </div>
                <div class="auth-separator">OR</div>
                <div class="auth-form">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button type="submit">Sign In</button>
                    <p>Don't have an account? <a href="#" style="color:#a770fa;">Sign Up</a></p>
                </div>
                <div class="auth-separator">OR</div>
                <div class="auth-form">
                    <input type="text" placeholder="Username">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button type="submit">Sign Up</button>
                    <p>Already have an account? <a href="#" style="color:#a770fa;">Sign In</a></p>
                </div>`;
        }
      }

      // Function to close the login modal
      function closeLoginModal() {
        loginModal.style.display = "none";
      }

      // Close the modal if the user clicks outside of it
      window.onclick = function (event) {
        if (event.target == loginModal) {
          loginModal.style.display = "none";
        }
      };

      function toggleLanguages(header) {
        const content = header.nextElementSibling;
        const languageButtons = content.querySelector(".language-buttons");
        const paragraph = content.querySelector("p");

        header.classList.toggle("open");

        if (header.classList.contains("open")) {
          languageButtons.style.display = "flex";
          paragraph.style.display = "none";
        } else {
          languageButtons.style.display = "none";
          paragraph.style.display = "block";
        }
      }

      // Get the projects modal
      var projectsModal = document.getElementById("projectsModal");

      // Function to show the projects modal
      function showProjects() {
        projectsModal.classList.add("show");
        document.body.style.overflow = "hidden";
      }

      // Function to close the projects modal
      function closeProjectsModal() {
        projectsModal.classList.remove("show");
        document.body.style.overflow = "";
      }