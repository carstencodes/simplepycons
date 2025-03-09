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


class AndroidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "android"

    @property
    def original_file_name(self) -> "str":
        return "android.svg"

    @property
    def title(self) -> "str":
        return "Android"

    @property
    def primary_color(self) -> "str":
        return "#3DDC84"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Android</title>
     <path d="M18.4395 5.5586c-.675 1.1664-1.352 2.3318-2.0274
 3.498-.0366-.0155-.0742-.0286-.1113-.043-1.8249-.6957-3.484-.8-4.42-.787-1.8551.0185-3.3544.4643-4.2597.8203-.084-.1494-1.7526-3.021-2.0215-3.4864a1.1451
 1.1451 0 0
 0-.1406-.1914c-.3312-.364-.9054-.4859-1.379-.203-.475.282-.7136.9361-.3886
 1.5019 1.9466 3.3696-.0966-.2158 1.9473
 3.3593.0172.031-.4946.2642-1.3926 1.0177C2.8987 12.176.452 14.772 0
 18.9902h24c-.119-1.1108-.3686-2.099-.7461-3.0683-.7438-1.9118-1.8435-3.2928-2.7402-4.1836a12.1048
 12.1048 0 0 0-2.1309-1.6875c.6594-1.122 1.312-2.2559
 1.9649-3.3848.2077-.3615.1886-.7956-.0079-1.1191a1.1001 1.1001 0 0
 0-.8515-.5332c-.5225-.0536-.9392.3128-1.0488.5449zm-.0391
 8.461c.3944.5926.324 1.3306-.1563
 1.6503-.4799.3197-1.188.0985-1.582-.4941-.3944-.5927-.324-1.3307.1563-1.6504.4727-.315
 1.1812-.1086 1.582.4941zM7.207 13.5273c.4803.3197.5506 1.0577.1563
 1.6504-.394.5926-1.1038.8138-1.584.4941-.48-.3197-.5503-1.0577-.1563-1.6504.4008-.6021
 1.1087-.8106 1.584-.4941z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://developer.android.com/distribute/mark'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
