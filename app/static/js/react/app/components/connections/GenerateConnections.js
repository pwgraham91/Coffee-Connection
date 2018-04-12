import PropTypes from 'prop-types';
import React from 'react';

export default class GenerateConnections extends React.Component {
  onClickGenerateConnections() {
    fetch(
      '/api/connections/generate_connections',
      {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      }
    )
    .then(response => response.json())
    .then(data => {
      console.log('generated', data)
    })
  }

  render() {
    return (
      <div>
        <button onClick={this.onClickGenerateConnections}>Generate Connections</button>
      </div>
    )
  }
}

GenerateConnections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

