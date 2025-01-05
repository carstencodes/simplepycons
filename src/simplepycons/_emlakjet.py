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


class EmlakjetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "emlakjet"

    @property
    def original_file_name(self) -> "str":
        return "emlakjet.svg"

    @property
    def title(self) -> "str":
        return "Emlakjet"

    @property
    def primary_color(self) -> "str":
        return "#0AE524"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Emlakjet</title>
     <path d="M15.65 16.105v-.24a3.543 3.543 0
 00-1.267-2.471c-.724-.663-1.69-.965-2.655-.904-1.87.12-3.378
 1.747-3.378 3.615 0 .784.12 1.567.422 2.471H4.55V6.946l7.42-5.123
 7.482
 5.122v11.692h-4.223c.18-.663.422-1.688.422-2.532m5.068-10.244L12.452.136c-.301-.181-.663-.181-.905
 0L3.222 5.86c-.242.12-.362.361-.362.663V19.48c0
 .482.362.844.844.844H9.92a.824.824 0 00.844-.844c0-.06
 0-.18-.06-.24l-.06-.182c-.302-.723-.664-1.627-.664-2.53v-.182c-.06-.542.12-1.084.482-1.446a2.095
 2.095 0 011.388-.723c.543-.06 1.026.12 1.448.482.422.362.664.844.724
 1.386v.18c.06 1.206-.724 2.954-.845 3.135l-1.146
 2.17-.18-.362c-.122-.181-.302-.362-.483-.422-.182-.06-.423-.06-.604.06-.18.12-.362.301-.422.482s-.06.422.06.603l.905
 1.687c.121.241.423.422.724.422.302 0
 .604-.18.724-.422l1.81-3.375h5.732a.824.824 0
 00.844-.843V6.524c-.06-.302-.18-.543-.422-.663" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.emlakjet.com/kurumsal-materyaller'''

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
