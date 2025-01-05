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


class ErlangIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "erlang"

    @property
    def original_file_name(self) -> "str":
        return "erlang.svg"

    @property
    def title(self) -> "str":
        return "Erlang"

    @property
    def primary_color(self) -> "str":
        return "#A90533"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Erlang</title>
     <path d="M8.859 7.889c.154-1.863 1.623-3.115 3.344-3.119
 1.734.004 2.986 1.256 3.029 3.119zm12.11 11.707c.802-.86 1.52-1.872
 2.172-3.03l-3.616-1.807c-1.27 2.064-3.127 3.965-5.694
 3.977-3.738-.012-5.206-3.208-5.198-7.322h13.966c.019-.464.019-.68
 0-.904.091-2.447-.558-4.504-1.737-6.106l-.007.005H24v15.186h-3.039zm-17.206-.001C1.901
 17.62.811 14.894.813 11.64c-.002-2.877.902-5.35
 2.456-7.232H0v15.187h3.761Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/erlang/erlide_eclipse/blob'''

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
