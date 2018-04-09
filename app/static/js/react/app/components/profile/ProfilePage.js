import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import Greeting from './Greeting';

class ProfilePage extends React.Component {
  componentDidMount() {
    fetch(`/api/user/${this.props.match.params.number}`)
      .then(response => response.json())
      .then(data => this.setState(data))
  }

  render() {
    return (
      <div>
        <Greeting userID={this.props.match.params.number} userDetails={this.state} />
      </div>
    )
  }
}

ProfilePage.propTypes = {
  filter: PropTypes.string,
  onFilter: PropTypes.func,
  match: PropTypes.shape({
    params: PropTypes.shape({
      number: PropTypes.string
    })
  })
};

const mapStateToProps = (state) => {
  return {
    filter: state.filter
  };
};


export default connect(
  mapStateToProps,
)(ProfilePage);
