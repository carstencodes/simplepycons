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


class DucatiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ducati"

    @property
    def original_file_name(self) -> "str":
        return "ducati.svg"

    @property
    def title(self) -> "str":
        return "Ducati"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ducati</title>
     <path d="M23.14
 3.895c-.326-1.307-1.96-2.001-3.103-2.45C17.302.383 13.382-.19
 10.401.056c-2.94.245-6.738 1.062-8.575 2.45-.531.409-.899.776-1.021
 1.715C.56 6.222 1.499 9.203 2.07
 11c.163-.082.367-.327.857-.572.98-.49 2.164-.817 3.267-1.02 3.96-.817
 9.473-.9 13.597-.9.49 0 .98 0 1.43.042.449 0 .98.04
 1.429.04l.245-1.102c.204-1.02.49-2.573.245-3.593zM5.95 5.528c-.531
 1.674-2.083 1.43-3.634 1.43L3.05 3.69c.326-.04.898 0 1.265 0 .45 0
 .776 0 1.144.123.612.245.735.98.49 1.715zm1.837
 1.51c-.898.042-1.715-.162-1.551-1.142.04-.245.449-2.124.49-2.206h1.306c-.04.368-.204.94-.286
 1.307-.04.245-.081.408-.122.654-.04.204-.123.571.204.49.204-.041.245-.286.286-.49.122-.572.327-1.47.408-1.96H9.83c-.04.326-.163.816-.245
 1.143-.204 1.062-.204 2.123-1.797 2.205zm3.308 0c-1.103
 0-1.511-.693-1.266-1.755.367-1.756 2.205-1.92
 2.94-1.51.408.244.49.53.408
 1.102h-1.225c0-.164.041-.327-.081-.409-.123-.081-.327
 0-.409.082-.204.204-.53 1.43-.286
 1.593.286.204.49-.205.531-.409h1.225c-.081.817-.816 1.348-1.837
 1.307zm4.165-.08v-.49h-.94l-.244.53H12.81c.04-.122.735-1.43.857-1.633l.899-1.634h1.715l.367
 3.267c-.286-.04-1.225 0-1.388-.04zm3.757-2.41c-.082.163-.245.98-.286
 1.184-.082.327-.164.858-.286
 1.184h-1.307c-.04-.204.49-2.123.49-2.409h-.816l.204-.898h2.98c0
 .122-.163.816-.204.898l-.775.041zm1.837 2.41h-1.347L20.2
 3.69h1.306l-.653 3.267zm-2.327
 2.94c-1.266.122-2.45.244-3.635.408-2.245.326-4.573.898-6.451
 1.674-1.593.694-3.88 2.082-3.88 4.165 0
 .326.041.326.286.694.368.53.858 1.266 1.225 1.756 1.184 1.51 3.308
 4.124 4.982 5.063.49.286.898.49 1.51.204.45-.204.9-.53 1.226-.776
 2.164-1.755 4.982-5.349 6.288-7.758.899-1.674 1.715-3.716
 2.287-5.676-.368-.04-3.47.204-3.838.245zM15.219
 5.61V4.425c-.082.082-.49 1.021-.53 1.185zM4.194 4.425l-.408
 1.797c.571.041.735-.327.816-.776.123-.49.286-1.061-.408-1.02z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brandlogos.net/ducati-logo-vector-svg'''

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
