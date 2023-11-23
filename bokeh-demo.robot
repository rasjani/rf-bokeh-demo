*** Settings ***
Library    bkdemo

*** Test Cases ***
Bokeh Demo
  ${bokehfigure}=   Generate Figure
  Log Figure    ${bokehfigure}

