# Material Icon Element Generator

Automatically generate an Polymer icons element for new material design icons like rounded and sharp style.

## Usage

- `generate.py`: main script.
- `template.html`: the default template of the Polymer element.
- `config.json`: where all the options are provided.
  - `style`: the style you want. See [Icons - Material Design](https://material.io/tools/icons/). 'Round' and 'Sharp' tested.
  - `svgUrl`: just... the url template of svg...
  - `elementName`: the name of the output element
  - `template`: the template you want to use for generating the element
  - `icons`: the icons you want