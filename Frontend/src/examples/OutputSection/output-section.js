import * as React from 'react';
import Website from './Website/website';

import './output-section.scss';

export default class OutputSection extends React.Component{

  render() {
    const { children, direction, size } = this.props;

    return (
      <div id="output-section">
        <div className="output-header">
          <center> Output Section </center>
        </div>

        <Website />
        <Website />
        <Website />
        <Website />
        <Website />
        
      </div>
    );
  }

}
