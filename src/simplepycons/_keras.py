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


class KerasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keras"

    @property
    def original_file_name(self) -> "str":
        return "keras.svg"

    @property
    def title(self) -> "str":
        return "Keras"

    @property
    def primary_color(self) -> "str":
        return "#D00000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keras</title>
     <path d="M24 0H0v24h24V0zM8.45
 5.16l.2.17v6.24l6.46-6.45h1.96l.2.4-5.14 5.1 5.47
 7.94-.2.3h-1.94l-4.65-6.88-2.16
 2.08v4.6l-.19.2H7l-.2-.2V5.33l.17-.17h1.48z" />
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
