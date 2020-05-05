import * as React from 'react';
import './website.scss';

export default class Website extends React.Component{

  render() {

    return (
        <div className="websites-container">
          <div className="website">
            <div className="website-title">
              <a className="website-link" href="https://google.com" target="_blank"> SWOT ANALYSIS OF AMAZON </a>
            </div>

            <div className="website-description">
              Identifying areas of strength and weakness is the second main outcome of a readiness assessment. Strengths determine the teams and practices that are ready ...
            </div>

          </div>
        </div>
    );
  }

}
