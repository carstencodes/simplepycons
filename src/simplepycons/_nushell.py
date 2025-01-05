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


class NushellIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nushell"

    @property
    def original_file_name(self) -> "str":
        return "nushell.svg"

    @property
    def title(self) -> "str":
        return "Nushell"

    @property
    def primary_color(self) -> "str":
        return "#4E9A06"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nushell</title>
     <path d="M0 16.338h1.25v-5.7c.417-.624 1.205-1.309 2.127-1.309
 1.176 0 1.34.64 1.34
 2.247v4.762h1.25v-5.685c0-1.458-.67-2.32-2.202-2.32-.923
 0-1.964.46-2.59 1.264l-.103-1.1H0Zm10.177-7.842h-1.25v5.698c0
 1.46.745 2.307 2.263 2.307.921 0 1.889-.431 2.514-1.22l.104
 1.057h1.072V8.496h-1.25v5.773c-.432.67-1.265 1.25-2.129 1.25-.907
 0-1.324-.446-1.324-1.458zm8.11-.997-.61.952 5.251 3.229-5.251
 3.244.669.922L24 12.32v-1.28z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/nushell/nushell/blob/3016d'''

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
