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


class ChannelFourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "channel4"

    @property
    def original_file_name(self) -> "str":
        return "channel4.svg"

    @property
    def title(self) -> "str":
        return "Channel 4"

    @property
    def primary_color(self) -> "str":
        return "#AAFF89"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Channel 4</title>
     <path d="m14.309 0-.33.412v4.201l2.382-2.95zm-1.155 1.201L10.707
 4.22v8.674h2.447zm3.268 1.701-2.443 3.02v14.81h2.443zM9.887
 5.236l-6.201 7.657h3.142L9.887 9.12Zm-6.766
 8.48v2.444h10.033v-2.443Zm14.125 0v2.444h3.633v-2.443Zm-6.539
 3.268V24h2.443v-7.016Zm-3.271 4.573V24h2.443v-2.443zm6.543
 0V24h5.189v-2.443z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://mediaassets.channel4.com/guidelines/g'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://mediaassets.channel4.com/guidelines/g
uide/34286b7b-ea25-404d-a43b-e912fc85b0e0/page/8a2dd59a-51df-4f47-aa37'''

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
