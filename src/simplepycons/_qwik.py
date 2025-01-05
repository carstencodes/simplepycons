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


class QwikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qwik"

    @property
    def original_file_name(self) -> "str":
        return "qwik.svg"

    @property
    def title(self) -> "str":
        return "Qwik"

    @property
    def primary_color(self) -> "str":
        return "#AC7EF4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qwik</title>
     <path d="M7.5469 0a2.957 2.957 0 0 0-2.5606 1.4785L.5332
 9.1915a2.957 2.957 0 0 0 0 2.957l4.4531 7.7128A2.955 2.955 0 0 0
 7.547 21.338H12l8.5938
 2.6484c.2409.0742.4512-.1782.3359-.4023l-1.916-3.7227
 4.4531-7.7129a2.957 2.957 0 0 0 0-2.957l-4.4531-7.7129A2.957 2.957 0
 0 0 16.453 0zm0 .7656L17.7324 10.67l-1.8965 1.8985.5782 7.5332L6.2676
 10.67l2.371-2.373z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/BuilderIO/qwik/blob/c88e53
d49dc65020899d770338f4e51f3134611e/packages/docs/public/logos/qwik-log'''

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
