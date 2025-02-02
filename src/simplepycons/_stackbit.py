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


class StackbitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stackbit"

    @property
    def original_file_name(self) -> "str":
        return "stackbit.svg"

    @property
    def title(self) -> "str":
        return "Stackbit"

    @property
    def primary_color(self) -> "str":
        return "#207BEA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stackbit</title>
     <path d="M10.9488 2.306L1.1706 7.9673c-.784.4493-1.2385
 1.3261-1.1623 2.242v3.7743c-.0664.9275.406 1.8084 1.2066
 2.2495l9.7782 5.4725a2.2606 2.2606 0 002.2305
 0l9.5937-5.4725c.7883-.45 1.2477-1.329
 1.1752-2.2495v-3.7744c.0683-.9116-.3846-1.7816-1.1623-2.2325l-9.5937-5.6615A2.2646
 2.2646 0 0012.0845 2c-.3917 0-.7833.102-1.1357.306zm.7749
 14.0366l-9.7782-5.6615a.745.745 0
 01-.2884-.2951c-.1974-.3648-.0683-.824.2884-1.0259l9.7782-5.6615a.7242.7242
 0 01.738 0l9.5936 5.6747c.353.2086.474.6702.2703
 1.0314-.2037.3612-.6551.485-1.0082.2764l-9.2284-5.452-8.2765 4.7915
 8.638 5.001c.3567.2053.483.6675.2823
 1.032-.1361.2477-.3874.3868-.6462.3868a.7266.7266 0
 01-.363-.0978zm.0147 3.963L1.9602 14.833a.707.707 0
 01-.0815-.0457c-.3443-.2232-.4465-.6897-.2282-1.0419.2178-.352.6741-.4567
 1.0182-.2334l9.4203 5.2708 9.2376-5.2708c.3566-.2033.8068-.0723
 1.0055.2925.1987.365.0706.8252-.286 1.0285l-9.5937 5.4728a.7239.7239
 0 01-.714 0z" />
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
