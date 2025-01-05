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


class LgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lg"

    @property
    def original_file_name(self) -> "str":
        return "lg.svg"

    @property
    def title(self) -> "str":
        return "LG"

    @property
    def primary_color(self) -> "str":
        return "#A50034"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LG</title>
     <path d="M14.522
 14.078h3.27v1.33h-4.847v-6.83h1.577v5.5zm6.74-1.274h1.284v1.195c-.236.09-.698.18-1.137.18-1.42
 0-1.893-.721-1.893-2.186 0-1.398.45-2.221 1.869-2.221.791 0 1.24.248
 1.612.722l.982-.903c-.6-.855-1.646-1.114-2.629-1.114-2.208 0-3.368
 1.205-3.368 3.504 0 2.288 1.047 3.528 3.358 3.528 1.06 0 2.096-.27
 2.66-.665V11.53h-2.739v1.274zM5.291 6.709a5.29 5.29 0 1 1 0 10.582
 5.291 5.291 0 1 1 0-10.582m3.16 8.457a4.445 4.445 0 0 0
 1.31-3.161v-.242l-.22.001H6.596v.494h2.662l-.001.015a3.985 3.985 0 0
 1-3.965 3.708 3.95 3.95 0 0 1-2.811-1.165 3.952 3.952 0 0
 1-1.164-2.811c0-1.061.414-2.059 1.164-2.81a3.951 3.951 0 0 1
 2.81-1.164l.252.003v-.495l-.251-.003a4.475 4.475 0 0 0-4.47 4.469c0
 1.194.465 2.316 1.309 3.161a4.444 4.444 0 0 0 3.16 1.31 4.444 4.444 0
 0 0
 3.162-1.31m-2.91-1.297V9.644H5.04v4.72h1.556v-.495H5.543zm-1.265-3.552a.676.676
 0 1 0-.675.674.676.676 0 0 0 .675-.674" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.lg.com/global/our-brand/brand-exp'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.lg.com/global/our-brand/brand-exp'''

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
