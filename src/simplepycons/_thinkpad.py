#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class ThinkpadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thinkpad"

    @property
    def original_file_name(self) -> "str":
        return "thinkpad.svg"

    @property
    def title(self) -> "str":
        return "ThinkPad"

    @property
    def primary_color(self) -> "str":
        return "#EE2624"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ThinkPad</title>
     <path d="M7.002 7.891a.677.677 0 0 0-.106 1.05.699.699 0 0 0
 1.066-.103.675.675 0 0 0 .117-.379l.001-.001a.676.676 0 0
 0-.203-.483.701.701 0 0 0-.875-.084zm10.239.403a1.268 1.268 0 0
 0-.881-.342h-1.466v8.195h1.148v-3.559h.318c.675 0 1.27-.68
 1.27-1.337l-.001-2.106a1.222 1.222 0 0 0-.388-.851zm-.654 3.052c0
 .334-.283.334-.543.334V8.87h.158c.301 0 .384.198.384.71v1.766zm4.162
 4.798l.001-.001h-.001zm-1.384-6.666c-.848 0-1.376.407-1.376
 1.103v1.283h1.078v-.934c.009-.289-.023-.708.31-.708.307 0
 .256.506.256.724 0 1.639-1.65 1.023-1.65 2.308v2.207c0
 .498.247.763.755.763.417 0 .614-.141.859-.532h.068a.979.979 0 0 0
 .065.451h1.02v-5.559c-.001-.679-.536-1.106-1.385-1.106zm.304
 5.561a.315.315 0 0 1-.317.293.298.298 0 0 1-.107-.011.287.287 0 0
 1-.162-.134.257.257 0 0
 1-.03-.101v-1.713c.003-.328.287-.517.613-.693h.003v2.359zm3.268-7.109v2.039h-.027a1.054
 1.054 0 0 0-.842-.503c-.428
 0-.809.247-.809.722v5.253c-.013.551.371.782.809.782.322-.038.612-.212.798-.477h.071v.396H24V7.93h-1.063zm-.001
 6.992c-.013.352-.154.411-.326.411-.158
 0-.29-.102-.29-.411v-4.168c0-.259.097-.384.29-.384.158 0
 .313.039.326.391v4.161zM0
 8.951h1.09v7.169h1.177V8.951h1.078V7.92H0zm5.504.518a.84.84 0 0
 0-.799.475h-.046V7.905H3.604v8.224h1.064v-5.388c0-.174.046-.379.317-.379.245
 0
 .298.165.298.389v5.379H6.35v-5.602c0-.693-.116-1.059-.846-1.059zm1.352.083h1.06v6.583h-1.06zm3.448-.069a.883.883
 0 0
 0-.799.465h-.044v-.389H8.404v6.581h1.054v-5.334c0-.185.014-.43.342-.43.245
 0
 .282.22.282.43v5.336h1.068v-5.496c.001-.693.01-1.163-.846-1.163zm4.193.079H13.43l-.611
 3.033h-.101V7.928h-1.065v8.215h1.065v-3.476h.101l.622
 3.476h1.091l-.676-3.604z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
