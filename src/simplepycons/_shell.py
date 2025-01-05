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


class ShellIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shell"

    @property
    def original_file_name(self) -> "str":
        return "shell.svg"

    @property
    def title(self) -> "str":
        return "Shell"

    @property
    def primary_color(self) -> "str":
        return "#FFD500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shell</title>
     <path d="M12 .863C5.34.863 0 6.251 0 12.98c0 .996.038 1.374.246
 2.33l3.662 2.71.57 4.515h6.102l.326.227c.377.262.705.375
 1.082.375.352 0 .732-.101 1.024-.313l.39-.289h6.094l.563-4.515
 3.695-2.71c.208-.956.246-1.334.246-2.33C24 6.252 18.661.863 12
 .863zm.996 2.258c.9 0 1.778.224 2.512.649l-2.465 12.548
 3.42-12.062c1.059.36 1.863.941 2.508 1.814l.025.034-4.902 10.615
 5.572-9.713.033.03c.758.708 1.247 1.567 1.492 2.648l-6.195 7.666
 6.436-6.5.01.021c.253.563.417 1.36.417 1.996 0 .509-.024.712-.164
 1.25l-3.554 2.602-.467
 3.71h-4.475l-.517.395c-.199.158-.482.266-.682.266-.199
 0-.483-.108-.682-.266l-.517-.394H6.322l-.445-3.61-3.627-2.666c-.11-.436-.16-.83-.16-1.261
 0-.72.159-1.49.426-2.053l.013-.024 6.45 6.551L2.75
 9.621c.25-1.063.874-2.09 1.64-2.713l5.542 9.776L4.979 6.1c.555-.814
 1.45-1.455 2.546-1.827l3.424 12.069L8.355 3.816l.055-.03c.814-.45
 1.598-.657 2.457-.657.195 0 .286.004.528.03l.587
 13.05.46-13.059c.224-.025.309-.029.554-.029z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Shell_logo'''

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
