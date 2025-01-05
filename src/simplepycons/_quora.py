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


class QuoraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quora"

    @property
    def original_file_name(self) -> "str":
        return "quora.svg"

    @property
    def title(self) -> "str":
        return "Quora"

    @property
    def primary_color(self) -> "str":
        return "#B92B27"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quora</title>
     <path d="M7.3799.9483A11.9628 11.9628 0 0 1 21.248 19.5397l2.4096
 2.4225c.7322.7362.21 1.9905-.8272 1.9905l-10.7105.01a12.52 12.52 0 0
 1-.304 0h-.02A11.9628 11.9628 0 0 1 7.3818.9503Zm7.3217 4.428a7.1717
 7.1717 0 1 0-5.4873 13.2512 7.1717 7.1717 0 0 0 5.4883-13.2511Z" />
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
