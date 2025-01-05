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


class MullvadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mullvad"

    @property
    def original_file_name(self) -> "str":
        return "mullvad.svg"

    @property
    def title(self) -> "str":
        return "Mullvad"

    @property
    def primary_color(self) -> "str":
        return "#294D73"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mullvad</title>
     <path d="M12 0C5.371 0 0 5.362 0 12c0 6.629 5.381 12 12
 12s12-5.371 12-12S18.629 0 12 0zm1.651 3.363c1.908-.02 4.059 1.28
 4.701 2.951.381 1 .267 2.086-.057 3.086-.266.819-1.238 2-.876
 2.886-.143-.038-3.124-1.048-3.98-1.505-1.344-.838-2.544-1.867-3.448-2.657l-.03-.029-3.047-1.447a1.037
 1.037 0 0 1-.104-.058c.419.029 2.085.23
 2.828.058-.143-.39-.105-.896.095-1.372.286-.657.83-1.095
 1.343-1.095.105 0 .2.019.296.057A3.411 3.411 0 0 1 12.39 3.6a3.49
 3.49 0 0 1 1.26-.237zm-2.499.97c-.457 0-.962.42-1.228
 1.02-.2.447-.229.933-.086 1.304a.813.813 0 0 0 .41.457.696.696 0 0 0
 .285.058c.457 0 .962-.42 1.22-1.02.161-.362.209-.742.152-1.076a.91.91
 0 0 0-.467-.676.6.6 0 0 0-.286-.067zm0 .286c.057 0
 .115.01.172.038.152.067.266.238.304.467.048.276.01.6-.133.905-.21.485-.619.838-.962.838a.444.444
 0 0
 1-.162-.029c-.142-.057-.219-.19-.257-.295-.114-.286-.085-.705.076-1.086.21-.495.62-.838.962-.838zM3.01
 6.362 2.943 7.79l.133.037.943-1.123-.648 1.104c1.01-.2 2.658-.247
 4.42-.114l1.837.895c.915.8 2.124 1.839 3.486 2.686l3.553
 1.4.438.638h-.372l.781.943-.714-.114c.01.066.714.876.714.876l-.562.076c.02.067.572.753.572.753l-.42-.03c.03.106.677
 1.153.677 1.163 0 .01-.229-.057-.381-.105.543 1.21 1.324 1.448 1.362
 1.943-2.667 3.419-9.667 3.952-12.771.124-.067-.314.619-.838
 1.057-1.429.21-.286.4-.59.533-.905.19-.58-.21-.533-.476-1.028-.047-.086-.086-.2-.047-.305.057-.19.38-.324.438-.286
 1.314.877 3.762.59 5.266-1.142 0 0
 .458.114.696.18l-.686-.457-.048-.028c-.028.019-.067.038-.095.057-3.124
 2.38-5.152 1.352-5.152 1.352a3.243 3.243 0 0
 0-.438-.39c-2.124-1.495-3.639-3.505-4.324-4.81l-.257
 1.381.057-1.838-.914
 1.276.676-1.371c-.505-.067-.79-.572-.676-.981.094-.426.63-.738
 1.096-.527z" />
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
        yield from [
            "Mullvad VPN",
        ]
