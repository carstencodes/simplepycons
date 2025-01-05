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


class GoogleTagManagerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googletagmanager"

    @property
    def original_file_name(self) -> "str":
        return "googletagmanager.svg"

    @property
    def title(self) -> "str":
        return "Google Tag Manager"

    @property
    def primary_color(self) -> "str":
        return "#246FDB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Tag Manager</title>
     <path d="M12.003 0a3 3 0 0 0-2.121 5.121l6.865 6.865-4.446 4.541
 1.745 1.836a3.432 3.432 0 0 1 .7.739l.012.011-.001.002a3.432 3.432 0
 0 1 .609 1.953 3.432 3.432 0 0
 1-.09.78l7.75-7.647c.031-.029.067-.05.098-.08.023-.023.038-.052.06-.076a2.994
 2.994 0 0 0-.06-4.166l-9-9A2.99 2.99 0 0 0 12.003 0zM8.63 2.133L.88
 9.809a2.998 2.998 0 0 0 0 4.238l7.7 7.75a3.432 3.432 0 0 1-.077-.729
 3.432 3.432 0 0 1 3.431-3.431 3.432 3.432 0 0 1 .826.101l-5.523-5.81
 4.371-4.373-2.08-2.08c-.903-.904-1.193-2.183-.898-3.342zm3.304
 16.004a2.932 2.932 0 0 0-2.931 2.931A2.932 2.932 0 0 0 11.934
 24a2.932 2.932 0 0 0 2.932-2.932 2.932 2.932 0 0 0-2.932-2.931z" />
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
