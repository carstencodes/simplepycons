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


class CastoramaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "castorama"

    @property
    def original_file_name(self) -> "str":
        return "castorama.svg"

    @property
    def title(self) -> "str":
        return "Castorama"

    @property
    def primary_color(self) -> "str":
        return "#0078D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Castorama</title>
     <path d="M8.91 16.106c-2.129 0-3.659-1.794-3.659-4.266 0-2.148
 1.468-4.095 3.488-4.095 2.275 0 3.545 1.857 3.545
 1.857l2.939-3.298c-.91-1.062-2.598-2.882-6.503-2.882-4.388 0-8.209
 3.489-8.209 8.456 0 4.766 3.475 8.532 8.266 8.532 3.855 0 5.572-2.017
 6.54-3.129l-2.831-2.969c0 .001-1.415 1.794-3.576 1.794zM18.283
 0v9.988h-2.064a1.92 1.92 0 1 0 0 3.84h2.064V24h5.205V0h-5.205z" />
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
