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


class OshkoshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oshkosh"

    @property
    def original_file_name(self) -> "str":
        return "oshkosh.svg"

    @property
    def title(self) -> "str":
        return "Oshkosh"

    @property
    def primary_color(self) -> "str":
        return "#E6830F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Oshkosh</title>
     <path d="M8.925 9.864V7.232c0-.414.183-.517.449-.517h5.335c.265 0
 .428.145.428.537v2.612h-1.57V8.657c0-.227 0-.29-.225-.29H10.72c-.246
 0-.246.063-.246.27v1.227h-1.55zm4.641 4.979v.48c0
 .226-.041.288-.224.288h-2.54c-.306 0-.327
 0-.327-.289v-.479h-1.55v1.925c0 .413.163.517.428.517h5.335c.245 0
 .449-.145.449-.538v-1.904h-1.57zm-2.036-1.905h.876v1.384h1.047V12.31c0-.087-.043-.433-.342-.433h-.534l.897-1.492h-1.111l-.833
 1.297v-1.297h-.983v3.937h.983v-1.384zm11.466-1.072h-.898v-1.47h-1.004v3.915h1.004v-1.298h.898v1.298H24v-3.915h-1.004v1.47zm-18.34-.043v-.39h1.773v-1.037H3.886a.381.381
 0 0 0-.385.367v1.73c0
 .217.086.37.278.37h1.496v.432H3.5v1.016h2.564c.214 0
 .364-.194.364-.41v-1.71a.362.362 0 0 0-.364-.368h-1.41zm14.07
 0v-.39h1.772v-1.037h-2.542a.381.381 0 0 0-.385.367v1.73c0
 .217.086.37.278.37h1.496v.432H17.57v1.016h2.564c.214 0
 .363-.194.363-.41v-1.71a.362.362 0 0
 0-.363-.368h-1.41zm-9.8.021H8.05v-1.448H7.024v3.915H8.05v-1.298h.876v1.298H9.95v-3.915H8.926v1.448zm-6.02-1.066v3.15c0
 .21-.173.383-.383.383H.383A.384.384 0 0 1 0
 13.928v-3.15c0-.21.172-.382.383-.382h2.14c.21 0 .383.172.383.382zm-1
 .804a.17.17 0 0 0-.17-.17H1.17a.17.17 0 0 0-.17.17v1.542c0
 .094.077.17.17.17h.567a.17.17 0 0 0 .17-.17v-1.542zm15.07-.804v3.15c0
 .21-.173.383-.383.383h-2.14a.384.384 0 0
 1-.383-.383v-3.15c0-.21.172-.382.383-.382h2.14c.21 0
 .382.172.382.382zm-1 .804a.17.17 0 0 0-.17-.17h-.567a.17.17 0 0
 0-.17.17v1.542c0 .094.076.17.17.17h.567a.17.17 0 0 0 .17-.17v-1.542z"
 />
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
