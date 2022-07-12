#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
"""prints colors"""

import argparse
import html.parser

# BASH_STR = 'printf "\x1b[38;5;XXXmcolourXXX YYY \x1b[0m\t";'
BASH_STR = "\x1b[38;5;XXXmcolourXXX YYY \x1b[0m\t"
BASH_ANSI_STR = "\\x1b[38;5;XXXm"
colo_list = []
LJUST_CONST = 4

COLORS = """<td>0</td><td>Black</td><td>#000000</td><td>rgb(0,0,0)</td><td>hsi(0,0%,0%)</td>
<td>1</td><td>Maroon</td><td>#800000</td><td>rgb(128,0,0)</td><td>hsi(0,100%,25%)</td>
<td>2</td><td>Green</td><td>#008000</td><td>rgb(0,128,0)</td><td>hsi(120,100%,25%)</td>
<td>3</td><td>Olive</td><td>#808000</td><td>rgb(128,128,0)</td><td>hsi(60,100%,25%)</td>
<td>4</td><td>Navy</td><td>#000080</td><td>rgb(0,0,128)</td><td>hsi(240,100%,25%)</td>
<td>5</td><td>Purple</td><td>#800080</td><td>rgb(128,0,128)</td><td>hsi(300,100%,25%)</td>
<td>6</td><td>Teal</td><td>#008080</td><td>rgb(0,128,128)</td><td>hsi(180,100%,25%)</td>
<td>7</td><td>Silver</td><td>#c0c0c0</td><td>rgb(192,192,192)</td><td>hsi(0,0%,75%)</td>
<td>8</td><td>Grey</td><td>#808080</td><td>rgb(128,128,128)</td><td>hsi(0,0%,50%)</td>
<td>9</td><td>Red</td><td>#ff0000</td><td>rgb(255,0,0)</td><td>hsi(0,100%,50%)</td>
<td>10</td><td>Lime</td><td>#00ff00</td><td>rgb(0,255,0)</td><td>hsi(120,100%,50%)</td>
<td>11</td><td>Yellow</td><td>#ffff00</td><td>rgb(255,255,0)</td><td>hsi(60,100%,50%)</td>
<td>12</td><td>Blue</td><td>#0000ff</td><td>rgb(0,0,255)</td><td>hsi(240,100%,50%)</td>
<td>13</td><td>Fuchsia</td><td>#ff00ff</td><td>rgb(255,0,255)</td><td>hsi(300,100%,50%)</td>
<td>14</td><td>Aqua</td><td>#00ffff</td><td>rgb(0,255,255)</td><td>hsi(180,100%,50%)</td>
<td>15</td><td>White</td><td>#ffffff</td><td>rgb(255,255,255)</td><td>hsi(0,0%,100%)</td>
<td>16</td><td>Grey0</td><td>#000000</td><td>rgb(0,0,0)</td><td>hsi(0,0%,0%)</td>
<td>17</td><td>NavyBlue</td><td>#00005f</td><td>rgb(0,0,95)</td><td>hsi(240,100%,18%)</td>
<td>18</td><td>DarkBlue</td><td>#000087</td><td>rgb(0,0,135)</td><td>hsi(240,100%,26%)</td>
<td>19</td><td>Blue3</td><td>#0000af</td><td>rgb(0,0,175)</td><td>hsi(240,100%,34%)</td>
<td>20</td><td>Blue3</td><td>#0000d7</td><td>rgb(0,0,215)</td><td>hsi(240,100%,42%)</td>
<td>21</td><td>Blue1</td><td>#0000ff</td><td>rgb(0,0,255)</td><td>hsi(240,100%,50%)</td>
<td>22</td><td>DarkGreen</td><td>#005f00</td><td>rgb(0,95,0)</td><td>hsi(120,100%,18%)</td>
<td>23</td><td>DeepSkyBlue4</td><td>#005f5f</td><td>rgb(0,95,95)</td><td>hsi(180,100%,18%)</td>
<td>24</td><td>DeepSkyBlue4</td><td>#005f87</td><td>rgb(0,95,135)</td><td>hsi(97,100%,26%)</td>
<td>25</td><td>DeepSkyBlue4</td><td>#005faf</td><td>rgb(0,95,175)</td><td>hsi(07,100%,34%)</td>
<td>26</td><td>DodgerBlue3</td><td>#005fd7</td><td>rgb(0,95,215)</td><td>hsi(13,100%,42%)</td>
<td>27</td><td>DodgerBlue2</td><td>#005fff</td><td>rgb(0,95,255)</td><td>hsi(17,100%,50%)</td>
<td>28</td><td>Green4</td><td>#008700</td><td>rgb(0,135,0)</td><td>hsi(120,100%,26%)</td>
<td>29</td><td>SpringGreen4</td><td>#00875f</td><td>rgb(0,135,95)</td><td>hsi(62,100%,26%)</td>
<td>30</td><td>Turquoise4</td><td>#008787</td><td>rgb(0,135,135)</td><td>hsi(180,100%,26%)</td>
<td>31</td><td>DeepSkyBlue3</td><td>#0087af</td><td>rgb(0,135,175)</td><td>hsi(93,100%,34%)</td>
<td>32</td><td>DeepSkyBlue3</td><td>#0087d7</td><td>rgb(0,135,215)</td><td>hsi(02,100%,42%)</td>
<td>33</td><td>DodgerBlue1</td><td>#0087ff</td><td>rgb(0,135,255)</td><td>hsi(08,100%,50%)</td>
<td>34</td><td>Green3</td><td>#00af00</td><td>rgb(0,175,0)</td><td>hsi(120,100%,34%)</td>
<td>35</td><td>SpringGreen3</td><td>#00af5f</td><td>rgb(0,175,95)</td><td>hsi(52,100%,34%)</td>
<td>36</td><td>DarkCyan</td><td>#00af87</td><td>rgb(0,175,135)</td><td>hsi(66,100%,34%)</td>
<td>37</td><td>LightSeaGreen</td><td>#00afaf</td><td>rgb(0,175,175)</td><td>hsi(180,100%,34%)</td>
<td>38</td><td>DeepSkyBlue2</td><td>#00afd7</td><td>rgb(0,175,215)</td><td>hsi(91,100%,42%)</td>
<td>39</td><td>DeepSkyBlue1</td><td>#00afff</td><td>rgb(0,175,255)</td><td>hsi(98,100%,50%)</td>
<td>40</td><td>Green3</td><td>#00d700</td><td>rgb(0,215,0)</td><td>hsi(120,100%,42%)</td>
<td>41</td><td>SpringGreen3</td><td>#00d75f</td><td>rgb(0,215,95)</td><td>hsi(46,100%,42%)</td>
<td>42</td><td>SpringGreen2</td><td>#00d787</td><td>rgb(0,215,135)</td><td>hsi(57,100%,42%)</td>
<td>43</td><td>Cyan3</td><td>#00d7af</td><td>rgb(0,215,175)</td><td>hsi(68,100%,42%)</td>
<td>44</td><td>DarkTurquoise</td><td>#00d7d7</td><td>rgb(0,215,215)</td><td>hsi(180,100%,42%)</td>
<td>45</td><td>Turquoise2</td><td>#00d7ff</td><td>rgb(0,215,255)</td><td>hsi(89,100%,50%)</td>
<td>46</td><td>Green1</td><td>#00ff00</td><td>rgb(0,255,0)</td><td>hsi(120,100%,50%)</td>
<td>47</td><td>SpringGreen2</td><td>#00ff5f</td><td>rgb(0,255,95)</td><td>hsi(42,100%,50%)</td>
<td>48</td><td>SpringGreen1</td><td>#00ff87</td><td>rgb(0,255,135)</td><td>hsi(51,100%,50%)</td>
<td>49</td><td>MediumSpringGreen</td><td>#00ffaf</td><td>rgb(0,255,175)</td><td>hsi(61,100%,50%)</td>
<td>50</td><td>Cyan2</td><td>#00ffd7</td><td>rgb(0,255,215)</td><td>hsi(70,100%,50%)</td>
<td>51</td><td>Cyan1</td><td>#00ffff</td><td>rgb(0,255,255)</td><td>hsi(180,100%,50%)</td>
<td>52</td><td>DarkRed</td><td>#5f0000</td><td>rgb(95,0,0)</td><td>hsi(0,100%,18%)</td>
<td>53</td><td>DeepPink4</td><td>#5f005f</td><td>rgb(95,0,95)</td><td>hsi(300,100%,18%)</td>
<td>54</td><td>Purple4</td><td>#5f0087</td><td>rgb(95,0,135)</td><td>hsi(82,100%,26%)</td>
<td>55</td><td>Purple4</td><td>#5f00af</td><td>rgb(95,0,175)</td><td>hsi(72,100%,34%)</td>
<td>56</td><td>Purple3</td><td>#5f00d7</td><td>rgb(95,0,215)</td><td>hsi(66,100%,42%)</td>
<td>57</td><td>BlueViolet</td><td>#5f00ff</td><td>rgb(95,0,255)</td><td>hsi(62,100%,50%)</td>
<td>58</td><td>Orange4</td><td>#5f5f00</td><td>rgb(95,95,0)</td><td>hsi(60,100%,18%)</td>
<td>59</td><td>Grey37</td><td>#5f5f5f</td><td>rgb(95,95,95)</td><td>hsi(0,0%,37%)</td>
<td>60</td><td>MediumPurple4</td><td>#5f5f87</td><td>rgb(95,95,135)</td><td>hsi(240,17%,45%)</td>
<td>61</td><td>SlateBlue3</td><td>#5f5faf</td><td>rgb(95,95,175)</td><td>hsi(240,33%,52%)</td>
<td>62</td><td>SlateBlue3</td><td>#5f5fd7</td><td>rgb(95,95,215)</td><td>hsi(240,60%,60%)</td>
<td>63</td><td>RoyalBlue1</td><td>#5f5fff</td><td>rgb(95,95,255)</td><td>hsi(240,100%,68%)</td>
<td>64</td><td>Chartreuse4</td><td>#5f8700</td><td>rgb(95,135,0)</td><td>hsi(7,100%,26%)</td>
<td>65</td><td>DarkSeaGreen4</td><td>#5f875f</td><td>rgb(95,135,95)</td><td>hsi(120,17%,45%)</td>
<td>66</td><td>PaleTurquoise4</td><td>#5f8787</td><td>rgb(95,135,135)</td><td>hsi(180,17%,45%)</td>
<td>67</td><td>SteelBlue</td><td>#5f87af</td><td>rgb(95,135,175)</td><td>hsi(210,33%,52%)</td>
<td>68</td><td>SteelBlue3</td><td>#5f87d7</td><td>rgb(95,135,215)</td><td>hsi(220,60%,60%)</td>
<td>69</td><td>CornflowerBlue</td><td>#5f87ff</td><td>rgb(95,135,255)</td><td>hsi(225,100%,68%)</td>
<td>70</td><td>Chartreuse3</td><td>#5faf00</td><td>rgb(95,175,0)</td><td>hsi(7,100%,34%)</td>
<td>71</td><td>DarkSeaGreen4</td><td>#5faf5f</td><td>rgb(95,175,95)</td><td>hsi(120,33%,52%)</td>
<td>72</td><td>CadetBlue</td><td>#5faf87</td><td>rgb(95,175,135)</td><td>hsi(150,33%,52%)</td>
<td>73</td><td>CadetBlue</td><td>#5fafaf</td><td>rgb(95,175,175)</td><td>hsi(180,33%,52%)</td>
<td>74</td><td>SkyBlue3</td><td>#5fafd7</td><td>rgb(95,175,215)</td><td>hsi(200,60%,60%)</td>
<td>75</td><td>SteelBlue1</td><td>#5fafff</td><td>rgb(95,175,255)</td><td>hsi(210,100%,68%)</td>
<td>76</td><td>Chartreuse3</td><td>#5fd700</td><td>rgb(95,215,0)</td><td>hsi(3,100%,42%)</td>
<td>77</td><td>PaleGreen3</td><td>#5fd75f</td><td>rgb(95,215,95)</td><td>hsi(120,60%,60%)</td>
<td>78</td><td>SeaGreen3</td><td>#5fd787</td><td>rgb(95,215,135)</td><td>hsi(140,60%,60%)</td>
<td>79</td><td>Aquamarine3</td><td>#5fd7af</td><td>rgb(95,215,175)</td><td>hsi(160,60%,60%)</td>
<td>80</td><td>MediumTurquoise</td><td>#5fd7d7</td><td>rgb(95,215,215)</td><td>hsi(180,60%,60%)</td>
<td>81</td><td>SteelBlue1</td><td>#5fd7ff</td><td>rgb(95,215,255)</td><td>hsi(195,100%,68%)</td>
<td>82</td><td>Chartreuse2</td><td>#5fff00</td><td>rgb(95,255,0)</td><td>hsi(7,100%,50%)</td>
<td>83</td><td>SeaGreen2</td><td>#5fff5f</td><td>rgb(95,255,95)</td><td>hsi(120,100%,68%)</td>
<td>84</td><td>SeaGreen1</td><td>#5fff87</td><td>rgb(95,255,135)</td><td>hsi(135,100%,68%)</td>
<td>85</td><td>SeaGreen1</td><td>#5fffaf</td><td>rgb(95,255,175)</td><td>hsi(150,100%,68%)</td>
<td>86</td><td>Aquamarine1</td><td>#5fffd7</td><td>rgb(95,255,215)</td><td>hsi(165,100%,68%)</td>
<td>87</td><td>DarkSlateGray2</td><td>#5fffff</td><td>rgb(95,255,255)</td><td>hsi(180,100%,68%)</td>
<td>88</td><td>DarkRed</td><td>#870000</td><td>rgb(135,0,0)</td><td>hsi(0,100%,26%)</td>
<td>89</td><td>DeepPink4</td><td>#87005f</td><td>rgb(135,0,95)</td><td>hsi(17,100%,26%)</td>
<td>90</td><td>DarkMagenta</td><td>#870087</td><td>rgb(135,0,135)</td><td>hsi(300,100%,26%)</td>
<td>91</td><td>DarkMagenta</td><td>#8700af</td><td>rgb(135,0,175)</td><td>hsi(86,100%,34%)</td>
<td>92</td><td>DarkViolet</td><td>#8700d7</td><td>rgb(135,0,215)</td><td>hsi(77,100%,42%)</td>
<td>93</td><td>Purple</td><td>#8700ff</td><td>rgb(135,0,255)</td><td>hsi(71,100%,50%)</td>
<td>94</td><td>Orange4</td><td>#875f00</td><td>rgb(135,95,0)</td><td>hsi(2,100%,26%)</td>
<td>95</td><td>LightPink4</td><td>#875f5f</td><td>rgb(135,95,95)</td><td>hsi(0,17%,45%)</td>
<td>96</td><td>Plum4</td><td>#875f87</td><td>rgb(135,95,135)</td><td>hsi(300,17%,45%)</td>
<td>97</td><td>MediumPurple3</td><td>#875faf</td><td>rgb(135,95,175)</td><td>hsi(270,33%,52%)</td>
<td>98</td><td>MediumPurple3</td><td>#875fd7</td><td>rgb(135,95,215)</td><td>hsi(260,60%,60%)</td>
<td>99</td><td>SlateBlue1</td><td>#875fff</td><td>rgb(135,95,255)</td><td>hsi(255,100%,68%)</td>
<td>100</td><td>Yellow4</td><td>#878700</td><td>rgb(135,135,0)</td><td>hsi(60,100%,26%)</td>
<td>101</td><td>Wheat4</td><td>#87875f</td><td>rgb(135,135,95)</td><td>hsi(60,17%,45%)</td>
<td>102</td><td>Grey53</td><td>#878787</td><td>rgb(135,135,135)</td><td>hsi(0,0%,52%)</td>
<td>103</td><td>LightSlateGrey</td><td>#8787af</td><td>rgb(135,135,175)</td><td>hsi(240,20%,60%)</td>
<td>104</td><td>MediumPurple</td><td>#8787d7</td><td>rgb(135,135,215)</td><td>hsi(240,50%,68%)</td>
<td>105</td><td>LightSlateBlue</td><td>#8787ff</td><td>rgb(135,135,255)</td><td>hsi(240,100%,76%)</td>
<td>106</td><td>Yellow4</td><td>#87af00</td><td>rgb(135,175,0)</td><td>hsi(3,100%,34%)</td>
<td>107</td><td>DarkOliveGreen3</td><td>#87af5f</td><td>rgb(135,175,95)</td><td>hsi(90,33%,52%)</td>
<td>108</td><td>DarkSeaGreen</td><td>#87af87</td><td>rgb(135,175,135)</td><td>hsi(120,20%,60%)</td>
<td>109</td><td>LightSkyBlue3</td><td>#87afaf</td><td>rgb(135,175,175)</td><td>hsi(180,20%,60%)</td>
<td>110</td><td>LightSkyBlue3</td><td>#87afd7</td><td>rgb(135,175,215)</td><td>hsi(210,50%,68%)</td>
<td>111</td><td>SkyBlue2</td><td>#87afff</td><td>rgb(135,175,255)</td><td>hsi(220,100%,76%)</td>
<td>112</td><td>Chartreuse2</td><td>#87d700</td><td>rgb(135,215,0)</td><td>hsi(2,100%,42%)</td>
<td>113</td><td>DarkOliveGreen3</td><td>#87d75f</td><td>rgb(135,215,95)</td><td>hsi(100,60%,60%)</td>
<td>114</td><td>PaleGreen3</td><td>#87d787</td><td>rgb(135,215,135)</td><td>hsi(120,50%,68%)</td>
<td>115</td><td>DarkSeaGreen3</td><td>#87d7af</td><td>rgb(135,215,175)</td><td>hsi(150,50%,68%)</td>
<td>116</td><td>DarkSlateGray3</td><td>#87d7d7</td><td>rgb(135,215,215)</td><td>hsi(180,50%,68%)</td>
<td>117</td><td>SkyBlue1</td><td>#87d7ff</td><td>rgb(135,215,255)</td><td>hsi(200,100%,76%)</td>
<td>118</td><td>Chartreuse1</td><td>#87ff00</td><td>rgb(135,255,0)</td><td>hsi(8,100%,50%)</td>
<td>119</td><td>LightGreen</td><td>#87ff5f</td><td>rgb(135,255,95)</td><td>hsi(105,100%,68%)</td>
<td>120</td><td>LightGreen</td><td>#87ff87</td><td>rgb(135,255,135)</td><td>hsi(120,100%,76%)</td>
<td>121</td><td>PaleGreen1</td><td>#87ffaf</td><td>rgb(135,255,175)</td><td>hsi(140,100%,76%)</td>
<td>122</td><td>Aquamarine1</td><td>#87ffd7</td><td>rgb(135,255,215)</td><td>hsi(160,100%,76%)</td>
<td>123</td><td>DarkSlateGray1</td><td>#87ffff</td><td>rgb(135,255,255)</td><td>hsi(180,100%,76%)</td>
<td>124</td><td>Red3</td><td>#af0000</td><td>rgb(175,0,0)</td><td>hsi(0,100%,34%)</td>
<td>125</td><td>DeepPink4</td><td>#af005f</td><td>rgb(175,0,95)</td><td>hsi(27,100%,34%)</td>
<td>126</td><td>MediumVioletRed</td><td>#af0087</td><td>rgb(175,0,135)</td><td>hsi(13,100%,34%)</td>
<td>127</td><td>Magenta3</td><td>#af00af</td><td>rgb(175,0,175)</td><td>hsi(300,100%,34%)</td>
<td>128</td><td>DarkViolet</td><td>#af00d7</td><td>rgb(175,0,215)</td><td>hsi(88,100%,42%)</td>
<td>129</td><td>Purple</td><td>#af00ff</td><td>rgb(175,0,255)</td><td>hsi(81,100%,50%)</td>
<td>130</td><td>DarkOrange3</td><td>#af5f00</td><td>rgb(175,95,0)</td><td>hsi(2,100%,34%)</td>
<td>131</td><td>IndianRed</td><td>#af5f5f</td><td>rgb(175,95,95)</td><td>hsi(0,33%,52%)</td>
<td>132</td><td>HotPink3</td><td>#af5f87</td><td>rgb(175,95,135)</td><td>hsi(330,33%,52%)</td>
<td>133</td><td>MediumOrchid3</td><td>#af5faf</td><td>rgb(175,95,175)</td><td>hsi(300,33%,52%)</td>
<td>134</td><td>MediumOrchid</td><td>#af5fd7</td><td>rgb(175,95,215)</td><td>hsi(280,60%,60%)</td>
<td>135</td><td>MediumPurple2</td><td>#af5fff</td><td>rgb(175,95,255)</td><td>hsi(270,100%,68%)</td>
<td>136</td><td>DarkGoldenrod</td><td>#af8700</td><td>rgb(175,135,0)</td><td>hsi(6,100%,34%)</td>
<td>137</td><td>LightSalmon3</td><td>#af875f</td><td>rgb(175,135,95)</td><td>hsi(30,33%,52%)</td>
<td>138</td><td>RosyBrown</td><td>#af8787</td><td>rgb(175,135,135)</td><td>hsi(0,20%,60%)</td>
<td>139</td><td>Grey63</td><td>#af87af</td><td>rgb(175,135,175)</td><td>hsi(300,20%,60%)</td>
<td>140</td><td>MediumPurple2</td><td>#af87d7</td><td>rgb(175,135,215)</td><td>hsi(270,50%,68%)</td>
<td>141</td><td>MediumPurple1</td><td>#af87ff</td><td>rgb(175,135,255)</td><td>hsi(260,100%,76%)</td>
<td>142</td><td>Gold3</td><td>#afaf00</td><td>rgb(175,175,0)</td><td>hsi(60,100%,34%)</td>
<td>143</td><td>DarkKhaki</td><td>#afaf5f</td><td>rgb(175,175,95)</td><td>hsi(60,33%,52%)</td>
<td>144</td><td>NavajoWhite3</td><td>#afaf87</td><td>rgb(175,175,135)</td><td>hsi(60,20%,60%)</td>
<td>145</td><td>Grey69</td><td>#afafaf</td><td>rgb(175,175,175)</td><td>hsi(0,0%,68%)</td>
<td>146</td><td>LightSteelBlue3</td><td>#afafd7</td><td>rgb(175,175,215)</td><td>hsi(240,33%,76%)</td>
<td>147</td><td>LightSteelBlue</td><td>#afafff</td><td>rgb(175,175,255)</td><td>hsi(240,100%,84%)</td>
<td>148</td><td>Yellow3</td><td>#afd700</td><td>rgb(175,215,0)</td><td>hsi(1,100%,42%)</td>
<td>149</td><td>DarkOliveGreen3</td><td>#afd75f</td><td>rgb(175,215,95)</td><td>hsi(80,60%,60%)</td>
<td>150</td><td>DarkSeaGreen3</td><td>#afd787</td><td>rgb(175,215,135)</td><td>hsi(90,50%,68%)</td>
<td>151</td><td>DarkSeaGreen2</td><td>#afd7af</td><td>rgb(175,215,175)</td><td>hsi(120,33%,76%)</td>
<td>152</td><td>LightCyan3</td><td>#afd7d7</td><td>rgb(175,215,215)</td><td>hsi(180,33%,76%)</td>
<td>153</td><td>LightSkyBlue1</td><td>#afd7ff</td><td>rgb(175,215,255)</td><td>hsi(210,100%,84%)</td>
<td>154</td><td>GreenYellow</td><td>#afff00</td><td>rgb(175,255,0)</td><td>hsi(8,100%,50%)</td>
<td>155</td><td>DarkOliveGreen2</td><td>#afff5f</td><td>rgb(175,255,95)</td><td>hsi(90,100%,68%)</td>
<td>156</td><td>PaleGreen1</td><td>#afff87</td><td>rgb(175,255,135)</td><td>hsi(100,100%,76%)</td>
<td>157</td><td>DarkSeaGreen2</td><td>#afffaf</td><td>rgb(175,255,175)</td><td>hsi(120,100%,84%)</td>
<td>158</td><td>DarkSeaGreen1</td><td>#afffd7</td><td>rgb(175,255,215)</td><td>hsi(150,100%,84%)</td>
<td>159</td><td>PaleTurquoise1</td><td>#afffff</td><td>rgb(175,255,255)</td><td>hsi(180,100%,84%)</td>
<td>160</td><td>Red3</td><td>#d70000</td><td>rgb(215,0,0)</td><td>hsi(0,100%,42%)</td>
<td>161</td><td>DeepPink3</td><td>#d7005f</td><td>rgb(215,0,95)</td><td>hsi(33,100%,42%)</td>
<td>162</td><td>DeepPink3</td><td>#d70087</td><td>rgb(215,0,135)</td><td>hsi(22,100%,42%)</td>
<td>163</td><td>Magenta3</td><td>#d700af</td><td>rgb(215,0,175)</td><td>hsi(11,100%,42%)</td>
<td>164</td><td>Magenta3</td><td>#d700d7</td><td>rgb(215,0,215)</td><td>hsi(300,100%,42%)</td>
<td>165</td><td>Magenta2</td><td>#d700ff</td><td>rgb(215,0,255)</td><td>hsi(90,100%,50%)</td>
<td>166</td><td>DarkOrange3</td><td>#d75f00</td><td>rgb(215,95,0)</td><td>hsi(6,100%,42%)</td>
<td>167</td><td>IndianRed</td><td>#d75f5f</td><td>rgb(215,95,95)</td><td>hsi(0,60%,60%)</td>
<td>168</td><td>HotPink3</td><td>#d75f87</td><td>rgb(215,95,135)</td><td>hsi(340,60%,60%)</td>
<td>169</td><td>HotPink2</td><td>#d75faf</td><td>rgb(215,95,175)</td><td>hsi(320,60%,60%)</td>
<td>170</td><td>Orchid</td><td>#d75fd7</td><td>rgb(215,95,215)</td><td>hsi(300,60%,60%)</td>
<td>171</td><td>MediumOrchid1</td><td>#d75fff</td><td>rgb(215,95,255)</td><td>hsi(285,100%,68%)</td>
<td>172</td><td>Orange3</td><td>#d78700</td><td>rgb(215,135,0)</td><td>hsi(7,100%,42%)</td>
<td>173</td><td>LightSalmon3</td><td>#d7875f</td><td>rgb(215,135,95)</td><td>hsi(20,60%,60%)</td>
<td>174</td><td>LightPink3</td><td>#d78787</td><td>rgb(215,135,135)</td><td>hsi(0,50%,68%)</td>
<td>175</td><td>Pink3</td><td>#d787af</td><td>rgb(215,135,175)</td><td>hsi(330,50%,68%)</td>
<td>176</td><td>Plum3</td><td>#d787d7</td><td>rgb(215,135,215)</td><td>hsi(300,50%,68%)</td>
<td>177</td><td>Violet</td><td>#d787ff</td><td>rgb(215,135,255)</td><td>hsi(280,100%,76%)</td>
<td>178</td><td>Gold3</td><td>#d7af00</td><td>rgb(215,175,0)</td><td>hsi(8,100%,42%)</td>
<td>179</td><td>LightGoldenrod3</td><td>#d7af5f</td><td>rgb(215,175,95)</td><td>hsi(40,60%,60%)</td>
<td>180</td><td>Tan</td><td>#d7af87</td><td>rgb(215,175,135)</td><td>hsi(30,50%,68%)</td>
<td>181</td><td>MistyRose3</td><td>#d7afaf</td><td>rgb(215,175,175)</td><td>hsi(0,33%,76%)</td>
<td>182</td><td>Thistle3</td><td>#d7afd7</td><td>rgb(215,175,215)</td><td>hsi(300,33%,76%)</td>
<td>183</td><td>Plum2</td><td>#d7afff</td><td>rgb(215,175,255)</td><td>hsi(270,100%,84%)</td>
<td>184</td><td>Yellow3</td><td>#d7d700</td><td>rgb(215,215,0)</td><td>hsi(60,100%,42%)</td>
<td>185</td><td>Khaki3</td><td>#d7d75f</td><td>rgb(215,215,95)</td><td>hsi(60,60%,60%)</td>
<td>186</td><td>LightGoldenrod2</td><td>#d7d787</td><td>rgb(215,215,135)</td><td>hsi(60,50%,68%)</td>
<td>187</td><td>LightYellow3</td><td>#d7d7af</td><td>rgb(215,215,175)</td><td>hsi(60,33%,76%)</td>
<td>188</td><td>Grey84</td><td>#d7d7d7</td><td>rgb(215,215,215)</td><td>hsi(0,0%,84%)</td>
<td>189</td><td>LightSteelBlue1</td><td>#d7d7ff</td><td>rgb(215,215,255)</td><td>hsi(240,100%,92%)</td>
<td>190</td><td>Yellow2</td><td>#d7ff00</td><td>rgb(215,255,0)</td><td>hsi(9,100%,50%)</td>
<td>191</td><td>DarkOliveGreen1</td><td>#d7ff5f</td><td>rgb(215,255,95)</td><td>hsi(75,100%,68%)</td>
<td>192</td><td>DarkOliveGreen1</td><td>#d7ff87</td><td>rgb(215,255,135)</td><td>hsi(80,100%,76%)</td>
<td>193</td><td>DarkSeaGreen1</td><td>#d7ffaf</td><td>rgb(215,255,175)</td><td>hsi(90,100%,84%)</td>
<td>194</td><td>Honeydew2</td><td>#d7ffd7</td><td>rgb(215,255,215)</td><td>hsi(120,100%,92%)</td>
<td>195</td><td>LightCyan1</td><td>#d7ffff</td><td>rgb(215,255,255)</td><td>hsi(180,100%,92%)</td>
<td>196</td><td>Red1</td><td>#ff0000</td><td>rgb(255,0,0)</td><td>hsi(0,100%,50%)</td>
<td>197</td><td>DeepPink2</td><td>#ff005f</td><td>rgb(255,0,95)</td><td>hsi(37,100%,50%)</td>
<td>198</td><td>DeepPink1</td><td>#ff0087</td><td>rgb(255,0,135)</td><td>hsi(28,100%,50%)</td>
<td>199</td><td>DeepPink1</td><td>#ff00af</td><td>rgb(255,0,175)</td><td>hsi(18,100%,50%)</td>
<td>200</td><td>Magenta2</td><td>#ff00d7</td><td>rgb(255,0,215)</td><td>hsi(09,100%,50%)</td>
<td>201</td><td>Magenta1</td><td>#ff00ff</td><td>rgb(255,0,255)</td><td>hsi(300,100%,50%)</td>
<td>202</td><td>OrangeRed1</td><td>#ff5f00</td><td>rgb(255,95,0)</td><td>hsi(2,100%,50%)</td>
<td>203</td><td>IndianRed1</td><td>#ff5f5f</td><td>rgb(255,95,95)</td><td>hsi(0,100%,68%)</td>
<td>204</td><td>IndianRed1</td><td>#ff5f87</td><td>rgb(255,95,135)</td><td>hsi(345,100%,68%)</td>
<td>205</td><td>HotPink</td><td>#ff5faf</td><td>rgb(255,95,175)</td><td>hsi(330,100%,68%)</td>
<td>206</td><td>HotPink</td><td>#ff5fd7</td><td>rgb(255,95,215)</td><td>hsi(315,100%,68%)</td>
<td>207</td><td>MediumOrchid1</td><td>#ff5fff</td><td>rgb(255,95,255)</td><td>hsi(300,100%,68%)</td>
<td>208</td><td>DarkOrange</td><td>#ff8700</td><td>rgb(255,135,0)</td><td>hsi(1,100%,50%)</td>
<td>209</td><td>Salmon1</td><td>#ff875f</td><td>rgb(255,135,95)</td><td>hsi(15,100%,68%)</td>
<td>210</td><td>LightCoral</td><td>#ff8787</td><td>rgb(255,135,135)</td><td>hsi(0,100%,76%)</td>
<td>211</td><td>PaleVioletRed1</td><td>#ff87af</td><td>rgb(255,135,175)</td><td>hsi(340,100%,76%)</td>
<td>212</td><td>Orchid2</td><td>#ff87d7</td><td>rgb(255,135,215)</td><td>hsi(320,100%,76%)</td>
<td>213</td><td>Orchid1</td><td>#ff87ff</td><td>rgb(255,135,255)</td><td>hsi(300,100%,76%)</td>
<td>214</td><td>Orange1</td><td>#ffaf00</td><td>rgb(255,175,0)</td><td>hsi(1,100%,50%)</td>
<td>215</td><td>SandyBrown</td><td>#ffaf5f</td><td>rgb(255,175,95)</td><td>hsi(30,100%,68%)</td>
<td>216</td><td>LightSalmon1</td><td>#ffaf87</td><td>rgb(255,175,135)</td><td>hsi(20,100%,76%)</td>
<td>217</td><td>LightPink1</td><td>#ffafaf</td><td>rgb(255,175,175)</td><td>hsi(0,100%,84%)</td>
<td>218</td><td>Pink1</td><td>#ffafd7</td><td>rgb(255,175,215)</td><td>hsi(330,100%,84%)</td>
<td>219</td><td>Plum1</td><td>#ffafff</td><td>rgb(255,175,255)</td><td>hsi(300,100%,84%)</td>
<td>220</td><td>Gold1</td><td>#ffd700</td><td>rgb(255,215,0)</td><td>hsi(0,100%,50%)</td>
<td>221</td><td>LightGoldenrod2</td><td>#ffd75f</td><td>rgb(255,215,95)</td><td>hsi(45,100%,68%)</td>
<td>222</td><td>LightGoldenrod2</td><td>#ffd787</td><td>rgb(255,215,135)</td><td>hsi(40,100%,76%)</td>
<td>223</td><td>NavajoWhite1</td><td>#ffd7af</td><td>rgb(255,215,175)</td><td>hsi(30,100%,84%)</td>
<td>224</td><td>MistyRose1</td><td>#ffd7d7</td><td>rgb(255,215,215)</td><td>hsi(0,100%,92%)</td>
<td>225</td><td>Thistle1</td><td>#ffd7ff</td><td>rgb(255,215,255)</td><td>hsi(300,100%,92%)</td>
<td>226</td><td>Yellow1</td><td>#ffff00</td><td>rgb(255,255,0)</td><td>hsi(60,100%,50%)</td>
<td>227</td><td>LightGoldenrod1</td><td>#ffff5f</td><td>rgb(255,255,95)</td><td>hsi(60,100%,68%)</td>
<td>228</td><td>Khaki1</td><td>#ffff87</td><td>rgb(255,255,135)</td><td>hsi(60,100%,76%)</td>
<td>229</td><td>Wheat1</td><td>#ffffaf</td><td>rgb(255,255,175)</td><td>hsi(60,100%,84%)</td>
<td>230</td><td>Cornsilk1</td><td>#ffffd7</td><td>rgb(255,255,215)</td><td>hsi(60,100%,92%)</td>
<td>231</td><td>Grey100</td><td>#ffffff</td><td>rgb(255,255,255)</td><td>hsi(0,0%,100%)</td>
<td>232</td><td>Grey3</td><td>#080808</td><td>rgb(8,8,8)</td><td>hsi(0,0%,3%)</td>
<td>233</td><td>Grey7</td><td>#121212</td><td>rgb(18,18,18)</td><td>hsi(0,0%,7%)</td>
<td>234</td><td>Grey11</td><td>#1c1c1c</td><td>rgb(28,28,28)</td><td>hsi(0,0%,10%)</td>
<td>235</td><td>Grey15</td><td>#262626</td><td>rgb(38,38,38)</td><td>hsi(0,0%,14%)</td>
<td>236</td><td>Grey19</td><td>#303030</td><td>rgb(48,48,48)</td><td>hsi(0,0%,18%)</td>
<td>237</td><td>Grey23</td><td>#3a3a3a</td><td>rgb(58,58,58)</td><td>hsi(0,0%,22%)</td>
<td>238</td><td>Grey27</td><td>#444444</td><td>rgb(68,68,68)</td><td>hsi(0,0%,26%)</td>
<td>239</td><td>Grey30</td><td>#4e4e4e</td><td>rgb(78,78,78)</td><td>hsi(0,0%,30%)</td>
<td>240</td><td>Grey35</td><td>#585858</td><td>rgb(88,88,88)</td><td>hsi(0,0%,34%)</td>
<td>241</td><td>Grey39</td><td>#626262</td><td>rgb(98,98,98)</td><td>hsi(0,0%,37%)</td>
<td>242</td><td>Grey42</td><td>#6c6c6c</td><td>rgb(108,108,108)</td><td>hsi(0,0%,40%)</td>
<td>243</td><td>Grey46</td><td>#767676</td><td>rgb(118,118,118)</td><td>hsi(0,0%,46%)</td>
<td>244</td><td>Grey50</td><td>#808080</td><td>rgb(128,128,128)</td><td>hsi(0,0%,50%)</td>
<td>245</td><td>Grey54</td><td>#8a8a8a</td><td>rgb(138,138,138)</td><td>hsi(0,0%,54%)</td>
<td>246</td><td>Grey58</td><td>#949494</td><td>rgb(148,148,148)</td><td>hsi(0,0%,58%)</td>
<td>247</td><td>Grey62</td><td>#9e9e9e</td><td>rgb(158,158,158)</td><td>hsi(0,0%,61%)</td>
<td>248</td><td>Grey66</td><td>#a8a8a8</td><td>rgb(168,168,168)</td><td>hsi(0,0%,65%)</td>
<td>249</td><td>Grey70</td><td>#b2b2b2</td><td>rgb(178,178,178)</td><td>hsi(0,0%,69%)</td>
<td>250</td><td>Grey74</td><td>#bcbcbc</td><td>rgb(188,188,188)</td><td>hsi(0,0%,73%)</td>
<td>251</td><td>Grey78</td><td>#c6c6c6</td><td>rgb(198,198,198)</td><td>hsi(0,0%,77%)</td>
<td>252</td><td>Grey82</td><td>#d0d0d0</td><td>rgb(208,208,208)</td><td>hsi(0,0%,81%)</td>
<td>253</td><td>Grey85</td><td>#dadada</td><td>rgb(218,218,218)</td><td>hsi(0,0%,85%)</td>
<td>254</td><td>Grey89</td><td>#e4e4e4</td><td>rgb(228,228,228)</td><td>hsi(0,0%,89%)</td>
<td>255</td><td>Grey93</td><td>#eeeeee</td><td>rgb(238,238,238)</td><td>hsi(0,0%,93%)</td>
"""


class Argparser:  # pylint: disable=too-few-public-methods
    """argparser class"""

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--ansi", action="store_true", help="bool", default=False
        )
        parser.add_argument(
            "--hsi", action="store_true", help="bool", default=False
        )
        parser.add_argument(
            "--rgb", action="store_true", help="bool", default=False
        )
        parser.add_argument(
            "--number", action="store_true", help="bool", default=False
        )
        parser.add_argument(
            "--name", action="store_true", help="bool", default=False
        )
        parser.add_argument(
            "--hex", action="store_true", help="bool", default=False
        )
        self.args = parser.parse_args()


class ColoParser(html.parser.HTMLParser):
    """html parser that ignores new lines"""

    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            colo_list.append(data)


def color_hsi(number_colo_list) -> str:
    """print hsi color codes"""
    print_list = str()
    hsi_colo_list = [
        colo_list[j] for j in range(0, len(colo_list)) if ((j + 1) % 5) == 0
    ]
    for i, number_colo in enumerate(number_colo_list):
        if i % 6 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", hsi_colo_list[i]
        )
    return print_list


def color_rgb(number_colo_list) -> str:
    """print rgb color codes"""
    print_list = str()
    rgb_colo_list = [
        colo_list[j] for j in range(0, len(colo_list)) if ((j + 1) % 5) == 4
    ]
    for i, number_colo in enumerate(number_colo_list):
        if i % 6 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", rgb_colo_list[i]
        )
    return print_list


def color_number(number_colo_list) -> str:
    """print color numbers"""
    print_list = str()
    for i, number_colo in enumerate(number_colo_list):
        if i % 12 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", number_colo
        )
    return print_list


def color_name(number_colo_list) -> str:
    """print color names"""
    print_list = str()
    name_colo_list = [
        colo_list[j] for j in range(0, len(colo_list)) if ((j + 1) % 5) == 2
    ]
    for i, number_colo in enumerate(number_colo_list):
        if i % 6 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", name_colo_list[i]
        )
    return print_list


def color_hex(number_colo_list) -> str:
    """print color hex codes"""
    print_list = str()
    hex_colo_list = [
        colo_list[j] for j in range(0, len(colo_list)) if ((j + 1) % 5) == 3
    ]
    for i, number_colo in enumerate(number_colo_list):
        if i % 8 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", hex_colo_list[i]
        )
    return print_list


def color_ansi(number_colo_list) -> str:
    """print color ansi escape sequnces"""
    print_list = str()
    for i, number_colo in enumerate(number_colo_list):
        if i % 6 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", BASH_ANSI_STR.replace("XXX", number_colo)
        )
    return print_list


def color_default(number_colo_list) -> str:
    """print numbers only"""
    print_list = str()
    for i, number_colo in enumerate(number_colo_list):
        if i % 12 == 0 and i != 0:
            print_list += "\n"
        print_list += BASH_STR.replace("XXX", number_colo).replace(
            "YYY", number_colo
        )
    return print_list


def colo() -> None:
    """prints the colors"""
    argparser = Argparser()
    print_list = str()
    lines = COLORS.split("\n")
    for line in lines:
        parser = ColoParser()
        parser.feed(line)
    number_colo_list = [
        colo_list[j] for j in range(0, len(colo_list)) if ((j + 1) % 5) == 1
    ]

    if argparser.args.hsi:
        print_list = color_hsi(number_colo_list)
    elif argparser.args.rgb:
        print_list = color_rgb(number_colo_list)
    elif argparser.args.number:
        print_list = color_number(number_colo_list)
    elif argparser.args.name:
        print_list = color_name(number_colo_list)
    elif argparser.args.hex:
        print_list = color_hex(number_colo_list)
    elif argparser.args.ansi:
        print_list = color_ansi(number_colo_list)
    else:
        print_list = color_default(number_colo_list)
    print(print_list)
