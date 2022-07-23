import React from 'react';

const Home: React.FC = () => {
  return (
    <div className='home'>
      <div className='content'>
        <div>
          <img src='/images/logo.png' className='logo' alt='' />
        </div>
        <button>Register</button>
        <p>Or</p>
        <button>Login</button>
      </div>

      <div className='bubbles'>
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
        <img src='/images/bubble.png' alt='' />
      </div>
    </div>
  );
};

export default Home;
