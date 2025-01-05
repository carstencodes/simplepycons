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


class RevancedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "revanced"

    @property
    def original_file_name(self) -> "str":
        return "revanced.svg"

    @property
    def title(self) -> "str":
        return "ReVanced"

    @property
    def primary_color(self) -> "str":
        return "#9ED5FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ReVanced</title>
     <path d="M5.1 0a.28.28 0 0 0-.23.42l6.88 11.93a.28.28 0 0 0 .48
 0L19.13.42A.28.28 0 0 0 18.9 0ZM.5 0a.33.33 0 0 0-.3.46L10.43
 23.8c.05.12.17.2.3.2h2.54c.13 0 .25-.08.3-.2L23.8.46a.33.33 0 0
 0-.3-.46h-2.32a.24.24 0 0 0-.21.14L12.2 20.08a.23.23 0 0 1-.42
 0L3.03.14A.23.23 0 0 0 2.82 0Z" />
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
