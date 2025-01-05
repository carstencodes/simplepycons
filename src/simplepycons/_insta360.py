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


class InstaThreeHundredAndSixtyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "insta360"

    @property
    def original_file_name(self) -> "str":
        return "insta360.svg"

    @property
    def title(self) -> "str":
        return "Insta360"

    @property
    def primary_color(self) -> "str":
        return "#FFEE00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Insta360</title>
     <path d="M15.402 11.19c-.701.7-1.838.7-2.54 0a1.796 1.796 0 1 1
 2.539 0m.998-3.614a6.17 6.17 0 0 0-4.39-1.818 6.17 6.17 0 0 0-4.392
 1.818 6.217 6.217 0 0 0 0 8.782 6.169 6.169 0 0 0 4.39 1.819 6.169
 6.169 0 0 0 4.392-1.82 6.217 6.217 0 0 0 0-8.78m1.554 10.33a8.353
 8.353 0 0 1-5.945 2.462 8.353 8.353 0 0
 1-5.944-2.46c-3.277-3.277-3.277-8.607 0-11.883a8.353 8.353 0 0 1
 5.944-2.46 8.35 8.35 0 0 1 5.944 2.46c3.278 3.276 3.278 8.606 0
 11.882m4.51-11.293a20.81 20.81 0 0 1-.137-.292 2.779 2.779 0 0 1
 .485-3.007c.018-.014.08-.08.117-.118a.412.412 0 0 0 .053-.069.66.66 0
 0 0-.097-.81.296.296 0 0 0-.026-.02 1.113 1.113 0 0
 0-.18-.11l-.068-.034A19.08 19.08 0 0 0 9.71.443l-.016.022a11.708
 11.708 0 0 0-6.012 3.218c-3.75 3.75-4.44 9.403-2.065
 13.852.023.043.107.195.123.233a2.778 2.778 0 0 1-.556 2.919 4.39 4.39
 0 0 0-.072.08.66.66 0 0 0 0
 .934c.06.056.127.105.198.146l.01.006a19.08 19.08 0 0 0 13
 1.677v.002a11.708 11.708 0 0 0 5.997-3.216c3.709-3.708 4.423-9.277
 2.144-13.702" />
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
