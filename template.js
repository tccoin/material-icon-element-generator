import '@polymer/iron-icon/iron-icon.js';
import '@polymer/iron-iconset-svg/iron-iconset-svg.js';
import './klog-icons-license.js';
const containerKlogIcons = document.createElement('template');

containerKlogIcons.innerHTML = `<iron-iconset-svg name="icons" size="24">
<svg><defs>
{}
</defs></svg>
</iron-iconset-svg>`;

document.head.appendChild(containerKlogIcons.content);