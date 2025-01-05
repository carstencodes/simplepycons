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


class JustgivingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "justgiving"

    @property
    def original_file_name(self) -> "str":
        return "justgiving.svg"

    @property
    def title(self) -> "str":
        return "JustGiving"

    @property
    def primary_color(self) -> "str":
        return "#AD29B6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JustGiving</title>
     <path d="M23.716 9.925H15.33l-4.898 4.919h6.727c-.885 1.975-2.865
 3.061-5.16 3.061-3.104 0-5.639-2.67-5.639-5.771C6.36 9.02 8.896 6.42
 12 6.42c1.134 0 2.189.295 3.061.871l4.542-4.561C17.541 1.031 14.893 0
 12 0 5.37 0 0 5.367 0 12c0 6.623 5.37 12 12 12s12-5.115
 12-11.738c0-.896-.103-1.35-.284-2.337z" />
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
