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


class ForgejoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "forgejo"

    @property
    def original_file_name(self) -> "str":
        return "forgejo.svg"

    @property
    def title(self) -> "str":
        return "Forgejo"

    @property
    def primary_color(self) -> "str":
        return "#FB923C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Forgejo</title>
     <path d="M16.7773 0c1.6018 0 2.9004 1.2986 2.9004 2.9005s-1.2986
 2.9004-2.9004 2.9004c-1.0854
 0-2.0315-.596-2.5288-1.4787H12.91c-2.3322 0-4.2272 1.8718-4.2649
 4.195l-.0007 2.1175a7.0759 7.0759 0 0 1 4.148-1.4205l.1176-.001
 1.3385.0002c.4973-.8827 1.4434-1.4788 2.5288-1.4788 1.6018 0 2.9004
 1.2986 2.9004 2.9005s-1.2986 2.9004-2.9004 2.9004c-1.0854
 0-2.0315-.596-2.5288-1.4787H12.91c-2.3322 0-4.2272 1.8718-4.2649
 4.195l-.0007 2.319c.8827.4973 1.4788 1.4434 1.4788 2.5287 0
 1.602-1.2986 2.9005-2.9005 2.9005-1.6018
 0-2.9004-1.2986-2.9004-2.9005 0-1.0853.596-2.0314
 1.4788-2.5287l-.0002-9.9831c0-3.887 3.1195-7.0453
 6.9915-7.108l.1176-.001h1.3385C14.7458.5962 15.692 0 16.7773
 0ZM7.2227 19.9052c-.6596 0-1.1943.5347-1.1943 1.1943s.5347 1.1943
 1.1943 1.1943 1.1944-.5347
 1.1944-1.1943-.5348-1.1943-1.1944-1.1943Zm9.5546-10.4644c-.6596
 0-1.1944.5347-1.1944 1.1943s.5348 1.1943 1.1944 1.1943c.6596 0
 1.1943-.5347
 1.1943-1.1943s-.5347-1.1943-1.1943-1.1943Zm0-7.7346c-.6596
 0-1.1944.5347-1.1944 1.1943s.5348 1.1943 1.1944 1.1943c.6596 0
 1.1943-.5347 1.1943-1.1943s-.5347-1.1943-1.1943-1.1943Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://codeberg.org/forgejo/meta/src/branch/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://codeberg.org/forgejo/meta/raw/branch/'''

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
