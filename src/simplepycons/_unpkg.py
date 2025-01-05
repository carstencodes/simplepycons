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


class UnpkgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unpkg"

    @property
    def original_file_name(self) -> "str":
        return "unpkg.svg"

    @property
    def title(self) -> "str":
        return "unpkg"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>unpkg</title>
     <path d="M0 0v24h24V0H0zm4.322 2.977 4.37.002a.043.043 0 0 1
 .044.04 9542.6 9542.6 0 0 1 0 9.165c0 .75.029 1.403.09
 1.957.038.336.134.68.287 1.03.336.769.907 1.237 1.715 1.405.626.13
 1.258.127 1.893-.008 1.166-.248 1.813-1.268
 1.96-2.404.067-.513.1-1.186.1-2.018-.001-3.15-.001-6.188.002-9.119
 0-.033.017-.05.049-.05h4.338a.033.033 0 0 1 .033.033v9.869c0
 1.465-.17 2.918-.746 4.234-.777 1.775-2.323 2.836-4.195
 3.211-1.7.341-3.39.338-5.07-.013-2.226-.465-3.808-1.828-4.46-4.03-.249-.846-.389-1.708-.416-2.586a65.217
 65.217 0 0 1-.029-1.88c-.002-3.037-.002-5.97 0-8.801
 0-.024.011-.037.035-.037z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mjackson/unpkg/blob/af8c8d'''

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
