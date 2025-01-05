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


class CloudbeesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudbees"

    @property
    def original_file_name(self) -> "str":
        return "cloudbees.svg"

    @property
    def title(self) -> "str":
        return "CloudBees"

    @property
    def primary_color(self) -> "str":
        return "#1997B5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CloudBees</title>
     <path d="M6.87.283C3.081.283 0 3.32 0 7.05c0 3.732 3.082 6.767
 6.87 6.767h2.429v-3.495h-2.43c-1.83 0-3.319-1.468-3.319-3.272 0-1.804
 1.488-3.27 3.32-3.27.734 0 1.377.19 1.928.567l2.51-2.473C10.06.814
 8.58.284 6.87.284zm5.152 2.231c-.066-.005-.141.08-.35.252a.457.457 0
 0 0-.028.026L9.722 4.674c-.323.315-.29.203-.066.556a3.204 3.204 0 0 1
 .532 1.749v9.991c0 3.73 3.096 6.747 6.908 6.747C20.907 23.717 24 20.7
 24
 16.97c0-3.728-3.093-6.75-6.904-6.75H13.76V6.979c0-1.495-.512-3.002-1.436-4.158-.175-.203-.234-.3-.3-.307zm5.246
 11.209c1.762.088 3.168 1.502 3.168 3.247 0 1.802-1.5 3.264-3.342
 3.264s-3.335-1.477-3.335-3.28v-3.219h3.509z" />
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
