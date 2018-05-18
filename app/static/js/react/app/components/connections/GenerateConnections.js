import PropTypes from 'prop-types';
import React from 'react';
import Button from '@material-ui/core/Button';


export default class GenerateConnections extends React.Component {
  constructor(props) {
    super(props)
    this.onClickGenerateConnections = this.onClickGenerateConnections.bind(this)
  }
  onClickGenerateConnections() {
    const onGeneration = this.props.onGeneration
    fetch(
      '/api/connections/generate_connections',
      {
        method: 'POST',
        credentials: 'include',
      }
    )
    .then(response => response.json())
    .then(data => {
      onGeneration(data)
    })
  }

  render() {
    return (
      <Button variant="raised" color="primary" onClick={this.onClickGenerateConnections}>
        Generate Connections
      </Button>
    )
  }
}

GenerateConnections.propTypes = {
  userDetails: PropTypes.object,
  onGeneration: PropTypes.func
};

