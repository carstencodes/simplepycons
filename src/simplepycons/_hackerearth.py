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


class HackerearthIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hackerearth"

    @property
    def original_file_name(self) -> "str":
        return "hackerearth.svg"

    @property
    def title(self) -> "str":
        return "HackerEarth"

    @property
    def primary_color(self) -> "str":
        return "#2C3454"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HackerEarth</title>
     <path d="M18.447 20.936H5.553V19.66h12.894zM20.973
 0H9.511v6.51h.104c.986-1.276 2.206-1.4 3.538-1.306 1.967.117 3.89
 1.346 4.017 5.169v7.322c0 .089-.05.177-.138.177h-2.29c-.09
 0-.253-.082-.253-.177V10.6c0-1.783-.58-3.115-2.341-3.115-1.282
 0-2.637.892-2.637 2.77v7.417c0 .089-.008.072-.102.072h-2.29c-.09
 0-.29.022-.29-.072V0H3.178c-.843 0-1.581.673-1.581 1.515v20.996c0
 .843.738 1.489 1.58 1.489h17.797c.843 0 1.431-.646
 1.431-1.489V1.515c0-.842-.588-1.515-1.43-1.515" />
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
