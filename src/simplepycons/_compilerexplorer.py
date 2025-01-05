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


class CompilerExplorerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "compilerexplorer"

    @property
    def original_file_name(self) -> "str":
        return "compilerexplorer.svg"

    @property
    def title(self) -> "str":
        return "Compiler Explorer"

    @property
    def primary_color(self) -> "str":
        return "#67C52A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Compiler Explorer</title>
     <path d="M8.78
 14.147h8.914v1.657H8.78Zm0-2.94h7.355v1.657H8.78Zm0-2.943h8.914V9.92H8.78Zm13.203
 9.195a.656.656 0 0 1 0-.638c.13-.238.252-.476.366-.728a.271.271 0 0
 0-.249-.383h-2.166a.656.656 0 0 0-.552.297 7.59 7.59 0 0 1-.977 1.208
 7.323 7.323 0 0 1-5.21 2.156 7.321 7.321 0 0 1-5.208-2.157 7.32 7.32
 0 0 1-2.157-5.21c0-1.969.766-3.821 2.156-5.211a7.323 7.323 0 0 1
 5.21-2.156c1.967 0 3.819.766 5.21 2.157.368.369.696.783.976
 1.207.12.186.327.297.551.297H22.1a.273.273 0 0 0 .248-.383 9.894
 9.894 0 0 0-.365-.728.665.665 0 0 1 0-.638l.735-1.332a.663.663 0 0
 0-.11-.787l-1.836-1.836a.659.66 0 0 0-.787-.11l-1.335.738a.656.656 0
 0 1-.638-.004 9.767 9.768 0 0 0-2.005-.824.657.657 0 0
 1-.452-.449L15.131.48a.664.664 0 0 0-.635-.48h-2.598a.657.657 0 0
 0-.634.48l-.421 1.46a.657.657 0 0
 1-.452.448c-.697.203-1.37.48-2.005.828-.2.11-.438.11-.638.003L6.41
 2.484a.663.663 0 0 0-.787.11L3.788 4.432a.659.66 0 0 0-.11.787l.737
 1.335c.11.2.107.438-.003.638a9.767 9.768 0 0 0-.825 2.005.657.657 0 0
 1-.448.452l-1.46.42a.664.664 0 0 0-.479.635v2.599c0
 .293.193.556.48.635l1.459.42a.657.657 0 0 1 .448.453c.204.697.48
 1.37.828 2.004.11.2.11.438.004.64l-.738 1.334a.663.663 0 0 0
 .11.786l1.835 1.837a.659.66 0 0 0
 .787.11l1.335-.738c.2-.11.438-.107.638.003a9.767 9.768 0 0 0
 2.005.825c.217.062.39.23.452.448l.42
 1.46c.083.283.342.48.635.48h2.598a.657.657 0 0 0
 .635-.48l.421-1.46a.657.657 0 0 1 .452-.448 9.975 9.976 0 0 0
 2.004-.828.67.67 0 0 1
 .639-.004l1.335.739c.259.14.58.096.786-.11l1.836-1.837a.659.66 0 0 0
 .11-.787z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/compiler-explorer/infra/bl
ob/8d362efe7ddc24e6a625f7db671d0a6e7600e3c9/logo/icon/CompilerExplorer'''

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
