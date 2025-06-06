let $ = document

let password = $.getElementById("password")
let createAccount = $.getElementById("create-account")

document.addEventListener('DOMContentLoaded', function() {
    const createAccountLink = document.getElementById('create-account');
    const signInForm = document.getElementById('signin-form');
    const signUpForm = document.getElementById('signup-form');
    const title = document.querySelector('h1');

    function showSignUp() {
        // Update title and link text
        title.textContent = 'Create your account';
        createAccountLink.textContent = 'I have an account';
        
        // Hide sign in form with animation
        signInForm.classList.add('hidden');
        
        // Show sign up form with animation
        setTimeout(() => {
            signUpForm.classList.remove('hidden');
            signUpForm.style.opacity = '0';
            signUpForm.style.transform = 'translateX(100%)';
            
            // Force reflow
            signUpForm.offsetHeight;
            
            signUpForm.style.opacity = '1';
            signUpForm.style.transform = 'translateX(0)';
        }, 300);
    }

    function showSignIn() {
        // Update title and link text
        title.textContent = 'Sign in to your account';
        createAccountLink.textContent = 'create an account';
        
        // Hide sign up form with animation
        signUpForm.style.opacity = '0';
        signUpForm.style.transform = 'translateX(-100%)';
        
        setTimeout(() => {
            signUpForm.classList.add('hidden');
            
            // Show sign in form with animation
            signInForm.classList.remove('hidden');
            signInForm.style.opacity = '0';
            signInForm.style.transform = 'translateX(100%)';
            
            // Force reflow
            signInForm.offsetHeight;
            
            signInForm.style.opacity = '1';
            signInForm.style.transform = 'translateX(0)';
        }, 300);
    }

    createAccountLink.addEventListener('click', function() {
        if (createAccountLink.textContent.trim() === 'create an account') {
            showSignUp();
        } else {
            showSignIn();
        }
    });

    // Add form submission handlers
    const signUpFormElement = signUpForm.querySelector('form');
    signUpFormElement.addEventListener('submit', function(e) {
        e.preventDefault();
        // Here you would typically handle the sign up logic
        console.log('Sign up form submitted');
    });

    const signInFormElement = signInForm.querySelector('form');
    signInFormElement.addEventListener('submit', function(e) {
        e.preventDefault();
        // Here you would typically handle the sign in logic
        console.log('Sign in form submitted');
    });
});


