# Panorama CSS declarations



Typed Panorama style properties and helper declarations.

## VCSSStyleDeclaration

<details><summary>CSS properties</summary>

- [align](#align)
- [animation](#animation)
- [animationDelay](#animationdelay)
- [animationDirection](#animationdirection)
- [animationDuration](#animationduration)
- [animationFillMode](#animationfillmode)
- [animationIterationCount](#animationiterationcount)
- [animationName](#animationname)
- [animationTimingFunction](#animationtimingfunction)
- [backgroundColor](#backgroundcolor)
- [backgroundImage](#backgroundimage)
- [backgroundPosition](#backgroundposition)
- [backgroundRepeat](#backgroundrepeat)
- [backgroundSize](#backgroundsize)
- [blur](#blur)
- [border](#border)
- [borderBottom](#borderbottom)
- [borderBottomColor](#borderbottomcolor)
- [borderBottomLeftRadius](#borderbottomleftradius)
- [borderBottomRightRadius](#borderbottomrightradius)
- [borderBottomStyle](#borderbottomstyle)
- [borderBottomWidth](#borderbottomwidth)
- [borderColor](#bordercolor)
- [borderLeft](#borderleft)
- [borderLeftColor](#borderleftcolor)
- [borderLeftStyle](#borderleftstyle)
- [borderLeftWidth](#borderleftwidth)
- [borderRadius](#borderradius)
- [borderRight](#borderright)
- [borderRightColor](#borderrightcolor)
- [borderRightStyle](#borderrightstyle)
- [borderRightWidth](#borderrightwidth)
- [borderStyle](#borderstyle)
- [borderTop](#bordertop)
- [borderTopColor](#bordertopcolor)
- [borderTopLeftRadius](#bordertopleftradius)
- [borderTopRightRadius](#bordertoprightradius)
- [borderTopStyle](#bordertopstyle)
- [borderTopWidth](#bordertopwidth)
- [borderWidth](#borderwidth)
- [boxShadow](#boxshadow)
- [brightness](#brightness)
- [clip](#clip)
- [color](#color)
- [contextMenuArrowPosition](#contextmenuarrowposition)
- [contextMenuBodyPosition](#contextmenubodyposition)
- [contextMenuPosition](#contextmenuposition)
- [contrast](#contrast)
- [flowChildren](#flowchildren)
- [font](#font)
- [fontFamily](#fontfamily)
- [fontSize](#fontsize)
- [fontStyle](#fontstyle)
- [fontWeight](#fontweight)
- [height](#height)
- [horizontalAlign](#horizontalalign)
- [hueRotation](#huerotation)
- [letterSpacing](#letterspacing)
- [lineHeight](#lineheight)
- [margin](#margin)
- [marginBottom](#marginbottom)
- [marginLeft](#marginleft)
- [marginRight](#marginright)
- [marginTop](#margintop)
- [maxHeight](#maxheight)
- [maxWidth](#maxwidth)
- [minHeight](#minheight)
- [minWidth](#minwidth)
- [opacity](#opacity)
- [opacityMask](#opacitymask)
- [opacityMaskScrollDown](#opacitymaskscrolldown)
- [opacityMaskScrollUp](#opacitymaskscrollup)
- [opacityMaskScrollUpDown](#opacitymaskscrollupdown)
- [overflow](#overflow)
- [padding](#padding)
- [paddingBottom](#paddingbottom)
- [paddingLeft](#paddingleft)
- [paddingRight](#paddingright)
- [paddingTop](#paddingtop)
- [perspective](#perspective)
- [perspectiveOrigin](#perspectiveorigin)
- [position](#position)
- [preTransformRotate2d](#pretransformrotate2d)
- [preTransformScale2d](#pretransformscale2d)
- [S2MixBlendMode](#s2mixblendmode)
- [saturation](#saturation)
- [sound](#sound)
- [soundOut](#soundout)
- [textAlign](#textalign)
- [textDecoration](#textdecoration)
- [textOverflow](#textoverflow)
- [textShadow](#textshadow)
- [textTransform](#texttransform)
- [textureSampling](#texturesampling)
- [tooltipArrowPosition](#tooltiparrowposition)
- [tooltipBodyPosition](#tooltipbodyposition)
- [tooltipPosition](#tooltipposition)
- [transform](#transform)
- [transformOrigin](#transformorigin)
- [transition](#transition)
- [transitionDelay](#transitiondelay)
- [transitionDuration](#transitionduration)
- [transitionProperty](#transitionproperty)
- [transitionTimingFunction](#transitiontimingfunction)
- [uiScale](#uiscale)
- [uiScaleX](#uiscalex)
- [uiScaleY](#uiscaley)
- [uiScaleZ](#uiscalez)
- [verticalAlign](#verticalalign)
- [visibility](#visibility)
- [washColor](#washcolor)
- [whiteSpace](#whitespace)
- [width](#width)
- [x](#x)
- [y](#y)
- [z](#z)
- [zIndex](#zindex)

</details>

### align

Type: `string | null`

### animation

Type: `string | null`

### animationDelay

Type: `string | null`

### animationDirection

Type: `string | null`

### animationDuration

Type: `string | null`

### animationFillMode

Type: `string | null`

### animationIterationCount

Type: `string | null`

### animationName

Type: `string | null`

### animationTimingFunction

Type: `string | null`

### backgroundColor

Sets the background fill color/gradient/combination for a panel.

Examples:
background-color: #FFFFFFFF;
background-color: gradient( linear, 0% 0%, 0% 100%, from( #fbfbfbff ), to( #c0c0c0c0 ) );
background-color: gradient( linear, 0% 0%, 0% 100%, from( #fbfbfbff ), color-stop( 0.3, #ebebebff ), to( #c0c0c0c0 ) );
background-color: gradient( radial, 50% 50%, 0% 0%, 80% 80%, from( #00ff00ff ), to( #0000ffff ) );
background-color: #0d1c22ff, gradient( radial, 100% -0%, 100px -40px, 320% 270%, from( #3a464bff ), color-stop( 0.23, #0d1c22ff ), to( #0d1c22ff ) );

Type: `string | null`

### backgroundImage

Comma separated list of images or movies to draw in the background. Can specify "none" to not draw a background layer. Combined with background-position, background-size and background-repeat
values.

Example:
background-image: url("file://{images}/default.tga"), url( "file://{movies}/Background1080p.webm" );

Type: `string | null`

### backgroundPosition

Controls the horizontal and vertical placement of the background image, with the format: <left|center|right> <horizontal length> <top|center|bottom> <vertical length>

If length is a percent, the specified location within the image is positioned over that same specified position in the background. If the length is pixels, the top left corner is placed
relative to the provided alignment keywords (left, bottom, etc.). See examples for more details.

If 1 value is specified, the other value is assumed to be center. If 2 values are specified, the first value must be for horizontal placement and the second for vertical.

Examples:
// aligns the top left corner of the image with the top left corner of the panel (default)
background-position: 0% 0%;
// centers the image within the background (same as "center center")
background-position: center;
// aligns the bottom right corner of the image with the bottom right corner of the panel (same as "100% 100%")
background-position: right bottom;
// the top left corner of the image is placed 10px to the right of, 40px below the top left corner of the panel
background-position: left 10px top 40px;

Type: `string | null`

### backgroundRepeat

Controls if the background should be repeated in the horizontal and vertical directions.

Possible values per direction:
"repeat" - (default) Repeated in the specified direction until it fills the panel
"space" - Repeated as many times as required to fill the panel w/o being clipped. Space is added between images to to align first and last image with panel edges.
"round" - Repeated as many times as required to fill the panel w/o being clipped. The image is resized to align first and last image with panel edges.
"no-repeat" - Not repeated

Possible single values:
"repeat-x" - equals "repeat no-repeat"
"repeat-y" - equals "no-repeat repeat"

Examples:
background-repeat: repeat; // equals "repeat repeat" (default)
background-repeat: repeat space; // repeats horizontally, spaces vertically
background-repeat: no-repeat round; // 1 column of images, scaled to fit evenly

Type: `string | null`

### backgroundSize

Sets the horizontal and vertical dimensions used to draw the background image. Can be set in pixels, percent, "contains" to size down to panel dimensions or "auto" preserves the image aspect
ratio. By default, set to "auto" which preveres the image's original size.

Multiple background layers can be specified in a comma separated list, which are then combined with background-image, background-position, and background-repeat values.

Examples:
background-size: auto; // same as "auto auto" (default)
background-size: 100% 100%; // image fills the panel
background-size: 50% 75%; // image fills 50% of the panel's width, and 75% of the panel's height
background-size: 300px 200px; // image is drawn 300px wide, 200px tall

Type: `string | null`

### blur

Sets the amount of blur to apply to the panel and all it's children during composition.  Default is no blur, for now Gaussian is the only blur type and takes a horizontal standard deviation,
vertical standard deviation, and number of passes.  Good std deviation values are around 0-10, if 10 is still not intense enough consider more passes, but more than one pass is bad for perf.
As shorthand you can specify with just one value, which will be used for the standard deviation in both directions and 1 pass will be set.

Examples:
blur: gaussian( 2.5 );
blur: gaussian( 6, 6, 1 );

Type: `string | null`

### border

Shorthand for setting panel border. Specify width, style, and color.  Supported styles are: solid, none.

Examples:
border: 2px solid #111111FF;

Type: `string | null`

### borderBottom

Shorthand for setting the bottom panel border. Specify width, style, and color.  Supported styles are: solid, none.

Examples:
border-bottom: 2px solid #111111FF;

Type: `string | null`

### borderBottomColor

Specifies border color for the bottom edge of the panel.

Examples:
border-bottom-color: #111111FF;

Type: `string | null`

### borderBottomLeftRadius

Specifies border-radius for bottom-left corner which rounds off border and clips background/foreground content to rounded edge.  Takes 1 or 2 values in px or %, first value is horizontal
radii for elliptical corner, second is vertical radii, if only one is specified then horizontal/vertical will both be set and corner will be circular.

Examples:
border-bottom-left-radius: 2px 2px;
border-bottom-left-radius: 5%;

Type: `string | null`

### borderBottomRightRadius

Specifies border-radius for bottom-right corner which rounds off border and clips background/foreground content to rounded edge.  Takes 1 or 2 values in px or %, first value is horizontal
radii for elliptical corner, second is vertical radii, if only one is specified then horizontal/vertical will both be set and corner will be circular.

Examples:
border-bottom-right-radius: 2px 2px;
border-bottom-right-radius: 5%;

Type: `string | null`

### borderBottomStyle

Specifies border style for the bottom edge of the panel.

Examples:
border-bottom-style: solid;

Type: `string | null`

### borderBottomWidth

Specifies border width for the bottom edge of the panel.

Examples:
border-bottom-width: 2px;

Type: `string | null`

### borderColor

Specifies border color for panel.  If a single color value is set it applies to all sides, if 2 are set the first is top/bottom and the second is left/right, if all four are set then they are
top, right, bottom, left in order.

Examples:
border-color: #111111FF;
border-color: #FF0000FF #00FF00FF #0000FFFF #00FFFFFF;

Type: `string | null`

### borderLeft

Shorthand for setting the left panel border. Specify width, style, and color.  Supported styles are: solid, none.

Examples:
border-left: 2px solid #111111FF;

Type: `string | null`

### borderLeftColor

Specifies border color for the left edge of the panel.

Examples:
border-left-color: #111111FF;

Type: `string | null`

### borderLeftStyle

Specifies border style for the left edge of the panel.

Examples:
border-left-style: solid;

Type: `string | null`

### borderLeftWidth

Specifies border width for the left edge of the panel.

Examples:
border-left-width: 2px;

Type: `string | null`

### borderRadius

Shorthand to set border radius for all corners at once.  Border radius rounds off corners of the panel, adjusting the border to smoothly round and also clipping background image/color and
contents to the specified elliptical or circular values.  In this shorthand version you may specify a single value for all raddi, or horizontal / vertical separated by the '/' character.
For both horizontal and vertical you may specify 1 to 4 values in pixels or %, they will be taken in order as top-left, top-right, bottom-right, bottom-left radii values.

Examples:
// 2 px circular corners on all sides
border-radius: 2px;
// Perfect circular or elliptical panel (circular if box was square)
border-radius: 50% / 50%;
// 2 px horizontal radii 4px vertical elliptical corners on all sides
border-radius: 2px / 4px;
// All corners fully specified
border-radius: 2px 3px 4px 2px / 2px 3px 3px 2px;

Type: `string | null`

### borderRight

Shorthand for setting the right panel border. Specify width, style, and color.  Supported styles are: solid, none.

Examples:
border-right: 2px solid #111111FF;

Type: `string | null`

### borderRightColor

Specifies border color for the right edge of the panel.

Examples:
border-right-color: #111111FF;

Type: `string | null`

### borderRightStyle

Specifies border style for the right edge of the panel.

Examples:
border-right-style: solid;

Type: `string | null`

### borderRightWidth

Specifies border width for the right edge of the panel.

Examples:
border-right-width: 2px;

Type: `string | null`

### borderStyle

Specifies border style for panel.  If a single style value is set it applies to all sides, if 2 are set the first is top/bottom and the second is left/right, if all four are set then they are
top, right, bottom, left in order.

Examples:
border-style: solid;
border-style: solid none solid none;

Type: `string | null`

### borderTop

Shorthand for setting the top panel border. Specify width, style, and color.  Supported styles are: solid, none.

Examples:
border-top: 2px solid #111111FF;

Type: `string | null`

### borderTopColor

Specifies border color for the top edge of the panel.

Examples:
border-top-color: #111111FF;

Type: `string | null`

### borderTopLeftRadius

Specifies border-radius for top-left corner which rounds off border and clips background/foreground content to rounded edge.  Takes 1 or 2 values in px or %, first value is horizontal radii
for elliptical corner, second is vertical radii, if only one is specified then horizontal/vertical will both be set and corner will be circular.

Examples:
border-top-left-radius: 2px 2px;
border-top-left-radius: 5%;

Type: `string | null`

### borderTopRightRadius

Specifies border-radius for top-right corner which rounds off border and clips background/foreground content to rounded edge.  Takes 1 or 2 values in px or %, first value is horizontal radii
for elliptical corner, second is vertical radii, if only one is specified then horizontal/vertical will both be set and corner will be circular.

Examples:
border-top-right-radius: 2px 2px;
border-top-right-radius: 5%;

Type: `string | null`

### borderTopStyle

Specifies border style for the top edge of the panel.

Examples:
border-top-style: solid;

Type: `string | null`

### borderTopWidth

Specifies border width for the top edge of the panel.

Examples:
border-top-width: 2px;

Type: `string | null`

### borderWidth

Specifies border width for panel.  If a single width value is set it applies to all sides, if 2 are set the first is top/bottom and the second is left/right, if all four are set then they are
top, right, bottom, left in order.

Examples:
border-width: 1px;'
border-width: 20px 1px 20px 1px;

Type: `string | null`

### boxShadow

Specifies outer shadows for boxes, or inset shadows/glows.  The shadow shape will match the border box for the panel,so use border-radius to affect rounding.  Syntax takes optional 'inset',
optional 'fill' then color, and then horizontal offset pixels, vertical offset pixels, blur radius pixels, and spread distance in pixels. Inset means the shadow is an inner shadow/glow, fill
is validonly on outer shadows and means draw the shadow behind the entire box, not clipping it to outside the border area only.

Examples:
box-shadow: #ffffff80 4px 4px 8px 0px; // outer
box-shadow: fill #ffffff80 4px 4px 8px 0px; // outer, filled
box-shadow: inset #333333b0 0px 0px 8px 12px; // inner

Type: `string | null`

### brightness

Sets the brightness that applies to the panel and all it's children during composition. The value is a multiplier on the HSB brightness value.

Example:
brightness: 1.5;

Type: `string | null`

### clip

Specifies a clip region within the panel, where contents will be clipped at render time. This clipping has no impact on layout, and is fast and supported for transitions/animations. Radialclip
mode takes a center point, start angle and angular width of the revealed sector.

Example:
clip: rect( 10%, 90%, 90%, 10% );clip: radial( 50% %50, 0deg, 90deg );

Type: `string | null`

### color

Sets the foreground fill color/gradient/combination for a panel.  This color is the color used to render text within the panel.

Examples:
color: #FFFFFFFF;
color: gradient( linear, 0% 0%, 0% 100%, from( #cbcbcbff ), to( #a0a0a0a0 ) );

Type: `string | null`

### contextMenuArrowPosition

Specifies where to point the arrow of a context menu at on this panel. The first value controls how the arrow is positioned horizontally when the context menu is to the top or bottom of the
panel, and the second value controls how the arrow is positioned vertically when the context menu is to the left or right of the panel. Default is '50% 50%'.

Example:
context-menu-arrow-position: 25% 50%;

Type: `string | null`

### contextMenuBodyPosition

Specifies where to position the body of a context menu relative to this panel. The first value controls how the body is aligned horizontally when the context menu is to the top or bottom of
the panel, and the second value controls how the body is aligned vertically when the context menu is to the left or right of the panel. 0% means left/top aligned, 50% means center/middle
aligned, and 100% means right/bottom aligned. Default is '0% 0%'.

Example:
context-menu-body-position: 50% 100%;

Type: `string | null`

### contextMenuPosition

Specifies where to position a context menu relative to this panel. Valid options include 'left', 'top', 'right', and 'bottom'. List up to 4 positions to determine the order that positions are
tried if the context menu doesn't fully fit on screen. Default is 'right left bottom top'. If less than 4 positions are specified, the context menu first tries the opposite of the specified
position along the same axis before switching to the other axis.

Examples:
context-menu-position: bottom;
context-menu-position: left bottom;

Type: `string | null`

### contrast

Sets the contrast that applies to the panel and all it's children during composition.

Example:
contrast: 1.5;

Type: `string | null`

### flowChildren

Type: `string | null`

### font

Type: `string | null`

### fontFamily

Specifies the font face to use.

Examples:
font-family: Arial;
font-family: "Comic Sans MS";

Type: `string | null`

### fontSize

Specifies the target font face height in pixels.

Example:
font-size: 12;

Type: `string | null`

### fontStyle

Specifies the font style to use. Supported values are normal, and italic

Example:
font-style: normal;

Type: `'noraml' | 'italic' | null`

### fontWeight

Specifies the font weight to use. Supported values are light, thin, normal, medium, bold, and black.

Examples:
font-weight: normal;
font-weight: bold;
font-weight: thin;

Type: `'light' | 'thin' | 'normal' | 'medium' | 'bold' | 'black' | null`

### height

Sets the height for this panel. Possible values:
"fit-children" - Panel size is set to the required size of all children (default)
<pixels> - Any fixed pixel value (ex: "100px")
<percentage> - Percentage of parent height (ex: "100%")
"fill-parent-flow( <weight> )" - Fills to remaining parent width. If multiple children are set to this value, weight is used to determine final height. For example, if three children are set
to fill-parent-flow of 1.0 and the parent is 300px tall, each child will be 100px tall. (ex: "fill-parent-flow( 1.0 )" )
"width-percentage( <percentage> )" - Percentage of the panel's width, which allows you to enforce a particular aspect ratio.  The width cannot also be height-percentage.

Type: `'fit-children' | string | null`

### horizontalAlign

Type: `string | null`

### hueRotation

Sets the hue rotation to apply to the panel and all it's children during composition. Default of 0.0 means no adjustment, domain is in degrees.

Example:
hue-rotation: 180deg;

Type: `string | null`

### letterSpacing

Sets letter-spacing for text in a string. Possible values:
normal - no manual spacing
<pixels> - Any fixed pixel value (ex: "1px")

Type: `string | null`

### lineHeight

Specifies the line height (distance between top edge of line above and line below) to use for text.  By default this is unset and a value that matches the font-size reasonably will be used
automatically.

Example:
line-height: 20px;

Type: `string | null`

### margin

Type: `string | null`

### marginBottom

Type: `string | null`

### marginLeft

Type: `string | null`

### marginRight

Type: `string | null`

### marginTop

Type: `string | null`

### maxHeight

Type: `string | null`

### maxWidth

Type: `string | null`

### minHeight

Type: `string | null`

### minWidth

Type: `string | null`

### opacity

Sets the opacity or amount of transparency applied to the panel and all it's children during composition. Default of 1.0 means fully opaque, 0.0 means fully transparent.

Example:
opacity: 0.8;

Type: `string | null`

### opacityMask

Applies an image as an opacity mask that stretches to the panel bounds and fades out it's content based on the alpha channel. The second float value is an optional opacity value for the mask
itself, the image won't interpolate/cross-fade, but you can animate the opacity to fade the mask in/out. The -scroll-up, -scroll-down, and -scroll-up-down varients override the mask and apply
only when the various vertical scroll scenarios affect the panel based on the overflow property.

Examples:
opacity-mask: url( "file://{images}/upper_row_mask.tga" );
opacity-mask: url( "file://{images}/upper_row_mask.tga" ) 0.5;
opacity-mask-scroll-up: url( "file://{images}/upper_row_mask_up.tga" ) 0.5;
opacity-mask-scroll-down: url( "file://{images}/upper_row_mask_down.tga" ) 0.5;
opacity-mask-scroll-up-down: url( "file://{images}/upper_row_mask_up_down.tga" ) 0.5;

Type: `string | null`

### opacityMaskScrollDown

Type: `string | null`

### opacityMaskScrollUp

Type: `string | null`

### opacityMaskScrollUpDown

Type: `string | null`

### overflow

Specifies what to do with contents that overflow the available space for the panel. Possible values:
"squish" - Children are squished to fit within the panel's bounds if needed (default)
"clip" - Children maintain their desired size but their contents are clipped
"scroll" - Children maintain their desired size and a scrollbar is added to this panel

Examples:
overflow: squish squish; // squishes contents in horizontal and vertical directions
overflow: squish scroll; // scrolls contents in the Y direction

Type: `| 'squish' | 'clip' | 'scroll' | 'squish squish' | 'squish clip ' | 'squish scroll' | 'clip clip' | 'clip squish' | 'clip scroll' | 'scroll scroll' | 'scroll squish' | 'scroll clip' | null`

### padding

Type: `string | null`

### paddingBottom

Type: `string | null`

### paddingLeft

Type: `string | null`

### paddingRight

Type: `string | null`

### paddingTop

Type: `string | null`

### perspective

Sets the perspective depth space available for children of the panel.  Default of 1000 would mean that children at 1000px zpos are right at the viewers eye, -1000px are just out of view
distance faded to nothing.

Example:
perspective: 1000;

Type: `string | null`

### perspectiveOrigin

Sets the perspective origin which will be used when transforming children of this panel.  This can be thought of as the camera x/y position relative to the panel.

Example:
perspective-origin: 50% 50%;

Type: `string | null`

### position

Sets the x, y, z position for a panel. Must not be in a flowing layout.

Example:
position: 3% 20px 0px;

Type: `string | null`

### preTransformRotate2d

Sets 2 dimensional rotation degrees that apply to the quad for this panel prior to 3 dimensional transforms. This rotation applies without perspective and leaves the panel centered at the same
spot as it started.

Example:
pre-transform-rotate2d: 45deg;

Type: `string | null`

### preTransformScale2d

Sets 2 dimensional X/Y scale factors that apply to the quad for this panel prior to 3 dimensional transforms. This scaling applies without perspective and leaves the panel centered at the same
spot as it started. Default of 1.0 means no scaling, 0.5 would be half size.

Examples:
pre-transform-scale2d: 0.8
pre-transform-scale2d: 0.4, 0.6

Type: `string | null`

### S2MixBlendMode

Controls blending mode for the panel. See CSS mix-blend-mode docs on web, except normal for us is with alpha blending.

Examples:
-s2-mix-blend-mode: normal;
-s2-mix-blend-mode: multiply;
-s2-mix-blend-mode: screen;

Type: `string | null`

### saturation

Sets the amount of saturation to apply to the panel and all it's children during composition.  Default of 1.0 means no adjustment, 0.0 means fully desaturated to gray scale, greater than 1.0
means over-saturation.

Example:
saturation: 0.4;

Type: `string | null`

### sound

Specifies a sound name to play when this selector is applied.

Example:
sound: "whoosh_in";

Type: `string | null`

### soundOut

Specifies a sound name to play when this selector is removed.

Example:
sound-out: "whoosh_out";

Type: `string | null`

### textAlign

Specifies the text alignment for text within this panel, defaults to left.

Examples:
text-align: left;
text-align: right;
text-align: center;

Type: `'left' | 'right' | 'center' | null`

### textDecoration

Specifies the decoration for text within this panel, defaults to none. Possible values: none, underline, line-through.

Example:
text-decoration: underline;

Type: `'none' | 'underline' | 'line-through' | null`

### textOverflow

Controls truncation of text that doesn't fit in a panel.  "clip" means to simply truncate (on char boundaries), "ellipsis" means to end with '...', and "shrink" means to a
We default to ellipsis, which is contrary to the normal CSS spec.

Examples:
text-overflow: ellipsis;
text-overflow: clip;
text-overflow: shrink;

Type: `'ellipsis' | 'clip' | 'shrink' | null`

### textShadow

Specifies text shadows.  The shadow shape will match the text the panel can generate,and this is only meaningful for labels.  Syntax takes horizontal offset pixels, vertical offset pixels,
blur radius pixels, strength, and then shadow color.

Example:
text-shadow: 2px 2px 8px 3.0 #333333b0;

Type: `string | null`

### textTransform

Specifies the transform for text within this panel, defaults to none. Possible values: none, uppercase, lowercase.

Example:
text-transform: uppercase;

Type: `'none' | 'uppercase' | 'lowercase' | null`

### textureSampling

Controls texture sampling mode for the panel. Set to alpha-only to use the textures alpha data across all 3 color channels.

Examples:
texture-sampling: normal;
texture-sampling: alpha-only;

Type: `'normal' | 'alpha-only' | null`

### tooltipArrowPosition

Specifies where to point the arrow of a tooltip at on this panel. The first value controls how the arrow is positioned horizontally when the tooltip is to the top or bottom of the panel, and
the second value controls how the arrow is positioned vertically when the tooltip is to the left or right of the panel. Default is '50% 50%'.

Example:
tooltip-arrow-position: 25% 50%;

Type: `string | null`

### tooltipBodyPosition

Specifies where to position the body of a tooltip relative to this panel. The first value controls how the body is aligned horizontally when the tooltip is to the top or bottom of the panel,
and the second value controls how the body is aligned vertically when the tooltip is to the left or right of the panel. 0% means left/top aligned, 50% means center/middle aligned, and 100%
means right/bottom aligned. Default is '0% 0%'.

Example:
tooltip-body-position: 50% 100%;

Type: `string | null`

### tooltipPosition

Specifies where to position a tooltip relative to this panel. Valid options include 'left', 'top', 'right', and 'bottom'. List up to 4 positions to determine the order that positions are tried
if the tooltip doesn't fully fit on screen. Default is 'right left bottom top'. If less than 4 positions are specified, the tooltip first tries the opposite of the specified position along the
same axis before switching to the other axis.

Examples:
tooltip-position: bottom;
tooltip-position: left bottom;

Type: `string | null`

### transform

Sets the transforms to apply to the panel in 2d or 3d space.  You can combine various transforms (comma separated) and they will be applied in order to create a 4x4 3d transform matrix.
The possible operations are: translate3d( x, y, z ), translatex( x ), translatey( y ), translatez( z ), scale3d( x, y, z), rotate3d( x, y, z ), rotatex( x ), rotatey( y ), rotatez( z ).

Examples:
transform: translate3d( -100px, -100px, 0px );
transform: rotateZ( -32deg ) rotateX( 30deg ) translate3d( 125px, 520px, 230px );

Type: `string | null`

### transformOrigin

Sets the transform origin about which transforms will be applied.  Default is 50% 50% on the panel so a rotation/scale is centered.

Example:
transform-origin: 50% 50%

Type: `string | null`

### transition

Specifies which properties should transition smoothly to new values if a class/pseudo class changes the styles.  Also specifies duration, timing function, and delay.
Valid timing functions are: ease, ease-in, ease-out, ease-in-out, linear.

Example:
transition: position 2.0s ease-in-out 0.0s, perspective-origin 1.2s ease-in-out 0.8s;

Type: `string | null`

### transitionDelay

Specifies the delay in seconds to use for transition properties on this panel, if more than one comma delimited value is specified then the values are applied to each property specified in
'transition-property' in order.  If only one value is specified then it applies to all the properties specified in transition-property.

Examples:
transition-delay: 0.0s;
transition-delay: 0.0s, 1.2s;

Type: `string | null`

### transitionDuration

Specifies the durating in seconds to use for transition properties on this panel, if more than one comma delimited value is specified then the values are applied to each property specified in
'transition-property' in order.  If only one value is specified then it applies to all the properties specified in transition-property.

Examples:
transition-duration: 2.0s;
transition-duration: 2.0s, 1.2s, 1.2s, 4.0s, 2.0s;

Type: `string | null`

### transitionProperty

Specifies which properties should transition smoothly to new values if a class/pseudo class changes the styles.

Examples:
transition: position, transform, background-color;

Type: `string | null`

### transitionTimingFunction

Specifies the timing function to use for transition properties on this panel, if more than one comma delimited value is specified then the values are applied to each property specified in
'transition-property' in order.  If only one value is specified then it applies to all the properties specified in transition-property. Valid timing functions are: ease, ease-in, ease-out,
ease-in-out, linear.

Examples:
transition-timing-function: ease-in-out;
transition-timing-function: ease-in-out, linear;
transition-timing-function: cubic-bezier( 0.785, 0.385, 0.555, 1.505 );

Type: `string | null`

### uiScale

Specifies a scale to apply to this panel's layout and all descendants. This scale happens at the layout level ratherthan the bitmap level, so things like text will increase their font size
rather than just bitmap scaling.

Examples:
ui-scale: 150%; // 150% scaling for X, Y, and Z.
ui-scale: 50% 100% 150%; // 50% scaling for X, 100% for Y. 150% for Z.

Type: `string | null`

### uiScaleX

Specifies a scale to apply to this panel's layout and all descendants. This scale happens at the layout level ratherthan the bitmap level, so things like text will increase their font size
rather than just bitmap scaling.

Examples:
ui-scale: 150%; // 150% scaling for X, Y, and Z.
ui-scale: 50% 100% 150%; // 50% scaling for X, 100% for Y. 150% for Z.

Type: `string | null`

### uiScaleY

Specifies a scale to apply to this panel's layout and all descendants. This scale happens at the layout level ratherthan the bitmap level, so things like text will increase their font size
rather than just bitmap scaling.

Examples:
ui-scale: 150%; // 150% scaling for X, Y, and Z.
ui-scale: 50% 100% 150%; // 50% scaling for X, 100% for Y. 150% for Z.

Type: `string | null`

### uiScaleZ

Specifies a scale to apply to this panel's layout and all descendants. This scale happens at the layout level ratherthan the bitmap level, so things like text will increase their font size
rather than just bitmap scaling.

Examples:
ui-scale: 150%; // 150% scaling for X, Y, and Z.
ui-scale: 50% 100% 150%; // 50% scaling for X, 100% for Y. 150% for Z.

Type: `string | null`

### verticalAlign

Type: `string | null`

### visibility

Controls if the panel is visible and is included in panel layout. Possible values:
"visible" - panel is visible and included in layout (default)
"collapse" - panel is invisible and not included in layout

Type: `'visible' | 'collapse' | null`

### washColor

Specifies a 'wash' color, which means a color that will be blended over the panel and all it's children at composition time, tinting them.  The alpha value of the color determines the
intensity of the tinting.

Example:
wash-color: #39b0d325;

Type: `string | null`

### whiteSpace

Controls white-space wrapping on rendered text.  "normal" means wrap on whitespace, "nowrap" means do no wrapping at all.

Examples:
white-space: normal;
white-space: nowrap;

Type: `'normal' | 'nowrap' | null`

### width

Sets the width for this panel. Possible values:
"fit-children" - Panel size is set to the required size of all children (default)
<pixels> - Any fixed pixel value (ex: "100px")
<percentage> - Percentage of parent width (ex: "100%")
"fill-parent-flow( <weight> )" - Fills to remaining parent width. If multiple children are set to this value, weight is used to determine final width. For example, if three children are set
to fill-parent-flow of 1.0 and the parent is 300px wide, each child will be 100px wide. (ex: "fill-parent-flow( 1.0 )" )
"height-percentage( <percentage> )" - Percentage of the panel's height, which allows you to enforce a particular aspect ratio.  The height cannot also be width-percentage.

Type: `string | null`

### x

Sets the x, y, z position for a panel. Must not be in a flowing layout.

Example:
position: 3% 20px 0px;

Type: `string | null`

### y

Sets the x, y, z position for a panel. Must not be in a flowing layout.

Example:
position: 3% 20px 0px;

Type: `string | null`

### z

Sets the x, y, z position for a panel. Must not be in a flowing layout.

Example:
position: 3% 20px 0px;

Type: `string | null`

### zIndex

Sets the z-index for a panel, panels will be sorted and painted in order within a parent panel.
The sorting first sorts by the z-pos computed from position and transforms, then if panels have matching zpos zindex is used. z-index is different than z-pos in that it doesn't affect rendering perspective, just paint/hit-test ordering.
The default z-index value is 0, and any floating point value is accepted.

Example:
z-index: 1;

Type: `number | null`
