import React from 'react';

export default class WelcomeInfo extends React.Component {
  render() {
    return (
      <div>
        <h2>What is Coffee Connection?</h2>
        <p>Coffee Connections is an app that allows you to connect with coworkers across departments!</p>
        <p>It works by connecting with Namely so we know what department you're in and it will set up connections with
          people you haven't met through the app in other departments.</p>
        <p>Check back every Monday for new connections.</p>
        <p>When you have a connection, be sure to reach out to them to set up a time to meet.</p>
        <p>Common connections might be a walk to SaTen for coffee or hanging out after work at Friends and Allies.</p>
        <h2>How To Participate</h2>
        <p>Simply log in to sign up!</p>
        <p>We'll generate new connections for you every Monday so just check back then and start the conversation when you get a match!</p>
      </div>
    )
  }
}