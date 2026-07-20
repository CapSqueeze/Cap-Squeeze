
// Initialize Supabase Client
const SUPABASE_URL = 'https://ceszjffxeswpffjugnmj.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNlc3pqZmZ4ZXN3cGZmanVnbm1qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ0NzI5OTMsImV4cCI6MjEwMDA0ODk5M30.u0rL0jnqnICTc62DvUZ9wyriC2hZ7wFSCypr_4dMmbY';

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Check if user is logged in and update UI
async function checkUserSession() {
  const { data: { session } } = await supabaseClient.auth.getSession();
  
  const loginLinks = document.querySelectorAll('.login-link');
  const signupLinks = document.querySelectorAll('.signup-link');
  
  if (session) {
    // User is logged in
    loginLinks.forEach(link => {
      link.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        Dashboard
      `;
      link.href = "dashboard.html";
    });
    
    signupLinks.forEach(link => {
      link.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
        Log Out
      `;
      link.href = "#";
      link.addEventListener('click', async (e) => {
        e.preventDefault();
        await supabaseClient.auth.signOut();
        window.location.reload();
      });
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  checkUserSession();
  
  // Google Auth Button
  const googleBtns = document.querySelectorAll('.google-btn');
  googleBtns.forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const { data, error } = await supabaseClient.auth.signInWithOAuth({
        provider: 'google',
        options: {
          redirectTo: window.location.origin + '/dashboard.html'
        }
      });
      if (error) {
        console.error('Error logging in with Google:', error);
        alert('Google Login Error: ' + error.message);
      }
    });
  });

  // Email/Password Signup Form
  const signupForm = document.getElementById('signup-form');
  if (signupForm) {
    signupForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const email = document.getElementById('signup-email').value;
      const password = document.getElementById('signup-password').value;
      const name = document.getElementById('signup-name').value;
      
      const { data, error } = await supabaseClient.auth.signUp({
        email,
        password,
        options: {
          data: {
            full_name: name
          }
        }
      });
      
      if (error) {
        alert(error.message);
      } else {
        alert('Signup successful! Check your email for confirmation (if required), or try logging in.');
        window.location.href = 'dashboard.html';
      }
    });
  }

  // Email/Password Login Form
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const email = document.getElementById('login-email').value;
      const password = document.getElementById('login-password').value;
      
      const { data, error } = await supabaseClient.auth.signInWithPassword({
        email,
        password
      });
      
      if (error) {
        alert(error.message);
      } else {
        window.location.href = 'dashboard.html';
      }
    });
  }
});
