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


class PhabricatorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phabricator"

    @property
    def original_file_name(self) -> "str":
        return "phabricator.svg"

    @property
    def title(self) -> "str":
        return "Phabricator"

    @property
    def primary_color(self) -> "str":
        return "#4A5F88"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Phabricator</title>
     <path d="M23.18 10.018l-4.426-4.449C17.053 3.782 14.66 2.665 12
 2.665S6.947 3.783 5.246 5.568L.821 10.02a2.802 2.802 0 0 0 0
 3.962l4.542 4.578c1.692 1.711 4.04 2.773 6.637 2.773s4.945-1.062
 6.637-2.774l4.543-4.579a2.802 2.802 0 0 0 0-3.962zM12 19.384a7.384
 7.384 0 1 1 0-14.768 7.384 7.384 0 0 1 0
 14.768zm3.651-7.572l.999-1.014-.447-1.028H14.78l-.456-.45-.038-1.437-1.008-.431-1.01.998h-.624l-1.047-1.006-1.022.415.035
 1.406-.444.443-1.444-.014-.409 1.023 1.034 1.01.006.633-.996 1.007.44
 1.031 1.428-.002.456.453.016 1.422 1.068.447.965-1.009.636.01 1.028
 1.011 1.044-.423-.043-1.409.442-.44
 1.43.013.423-1.03-1.03-1-.009-.629zm-3.715 1.806a1.533 1.533 0 1 1
 0-3.065 1.533 1.533 0 0 1 0 3.065z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/phacility/phabricator/blob
/0a3093ef9c1898913196564435346e4daa9d2538/webroot/rsrc/image/logo/ligh'''

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
